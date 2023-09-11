import multiprocessing as mp
import os
import shutil
import subprocess
import tempfile
import time
from itertools import product

import pandas as pd

from hep_pheno_tools.analysis_tools import approx_global_sig
from stats import get_xgb_matrix

# Download the framework or update it
try:
    import hep_pheno_tools

    hep_pheno_tools.update()
except ImportError:
    user = "Phenomenology-group-uniandes"
    framework = "hep_pheno_tools"
    git_url = f"git@github.com:{user}/{framework}.git"
    subprocess.run(["git", "clone", git_url])
    import hep_pheno_tools

from signal_production.calculate_xs_matrices import get_xs_matrix

# Delete all the temp folders
[shutil.rmtree(f) for f in os.listdir(os.getcwd()) if "tmp" in f]

# Create a temporary directory
TEMP_DIR = tempfile.mkdtemp(dir=os.getcwd())
DATA_DIR = os.path.join(os.getcwd(), "data")
PARAMS_DIR = os.path.join(DATA_DIR, "param_cards")
xs_path = os.path.join(DATA_DIR, "cross_sections")
eff_path = os.path.join(DATA_DIR, "abs_efficiencies")
XGB_distros_path = os.path.join(DATA_DIR, "XGB_distros")
# Define the kinematic generation cuts
parton_kin_gen_cuts = {
    "cut_decays": True,
    "ptb": 30,
    "ptj": 20,
    "ptl": 20,
    "etab": 2.5,
    "pt_min_pdg": "{15: 30}",
    # "eta_max_pdg": '{15: 2.5}',
    # 'mxx_min_pdg': '{15:100}'
}

cases = ["woRHC", "wRHC"]
signal_production_channels = ["non-res", "sLQ", "dLQ"]

lower_mass = 500
upper_mass = 5000
mass_step = 250
lower_g_u = 0.5
upper_g_u = 3.5
g_u_step = 0.25
parton_n_events = 30000

n_workers = 2

bkg_groups = {
    "ttbar": ["ttbar"],
    "single_top": ["stop"],
    "Vjets": ["w_jets", "z_jets"],
    "VV": ["ww", "zz", "wz"],
}

signal_groups = {
    "non-res": ["non-res"],
    "sLQ": ["sLQ"],
    "dLQ": ["dLQ"],
}
channels = [
    "0b_2tau_hadronic",
    "0b_2tau_semileptonic",
    "1b_2tau_hadronic",
    "1b_2tau_semileptonic",
    "2b_2tau_hadronic",
    "2b_2tau_semileptonic",
]


# decorator to show the execution time of a function
def timer(func):
    def wrapper(*args, **kwargs):
        print(f"Running {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        hours, rem = divmod(elapsed, 3600)
        minutes, seconds = divmod(rem, 60)
        print(f"Elapsed time: {hours:.0f}h {minutes:.0f}m {seconds:.2f}s")
        return result

    return wrapper


def gen_csv_matrix(x):
    case, channel = x
    xs_matrix = get_xs_matrix(
        lower_mass=lower_mass,
        upper_mass=upper_mass,
        mass_step=mass_step,
        lower_g_u=lower_g_u,
        upper_g_u=upper_g_u,
        g_u_step=g_u_step,
        case=case,
        channel=channel,
        n_events=parton_n_events,
        test=False,
        param_cards_folder_path=PARAMS_DIR,
        temp_dir=TEMP_DIR,
        kin_gen_cuts=parton_kin_gen_cuts,
        n_workers=int(mp.cpu_count() / n_workers),
    )
    csv_path = os.path.join(
        DATA_DIR, "cross_sections", case, channel, "xs_matrix.csv"
    )
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    xs_matrix.to_csv(csv_path)
    xs_matrix.to_excel(csv_path.replace(".csv", ".xlsx"))


@timer
def gen_xs_matrices(cases, channels):
    print("Generating cross section matrices...")
    with mp.Pool() as pool:
        pool.map(gen_csv_matrix, product(cases, channels))
    pass


def get_bkg_events(channel, bkg_groups, luminosity=137):
    bkg_events = {}

    for group in bkg_groups:
        n_events = 0
        for bkg in bkg_groups[group]:
            bkg_xs = pd.read_excel(
                os.path.join(xs_path, "bkg_xs.xlsx"), index_col=0
            )
            bkg_xs = bkg_xs[bkg]["xs"]
            bkg_eff = pd.read_excel(
                os.path.join(eff_path, channel, "backgrounds.xlsx"),
                index_col=0,
            )
            eff = bkg_eff[bkg]["DeltaR > 0.3"]
            n_events += bkg_xs * eff * luminosity * 1000
        bkg_events[group] = n_events
    return bkg_events


def get_signal_events(
    channel, signal_groups, mass, coupling, case, luminosity=137
):
    signal_events = {}
    if mass < 1000:
        m = 1000
    elif mass > 2500:
        m = 2500
    else:
        m = mass
    for group in signal_groups:
        n_events = 0
        for signal in signal_groups[group]:
            signal_xs = pd.read_excel(
                os.path.join(xs_path, case, signal, "xs_matrix.xlsx"),
                index_col=0,
            )
            signal_xs = signal_xs[str(mass)][coupling]
            signal_eff = pd.read_excel(
                os.path.join(eff_path, channel, case, f"M{m}.xlsx"),
                index_col=0,
            )
            eff = signal_eff[signal]["DeltaR > 0.3"]
            n_events += signal_xs * eff * luminosity * 1000
        signal_events[group] = n_events
    return signal_events


signal_name = {
    "non-res": "tau_tau",
    "sLQ": "tau_Lq",
    "dLQ": "Lq_Lq",
}


def get_signal_channel_distros(
    channel, signal_groups, masses, gu_values, case
):
    signal_channel_distros = {}
    for key, value in signal_groups.items():
        matrix = get_xgb_matrix(
            signal_name[value[0]],
            channel,
            case,
            XGB_distros_path,
            masses,
            gu_values,
            integral=1.0,
        )
        for (i, mass), (j, gu) in product(
            enumerate(masses), enumerate(gu_values)
        ):
            signal_events = get_signal_events(
                channel, signal_groups, mass, gu, case
            )[key]
            # matrix[mass][gu] *= signal_events
            matrix[i][j] *= signal_events
        signal_channel_distros[key] = matrix

    return signal_channel_distros


def concatenate_distros_matrices(distros_matrices: list):
    """
    let X[i][j] and Y[i][j] two distribution matrices for two different
    channels but for the same signal, where i is the index of mass and j is
    the index of gu. Each entry is a distribution of X[i][j]. This function
    returns a new matrix T[i][j] = concatenate(X[i][j], Y[i][j], ...).
    """
    x_shape, y_shape, z_shape = distros_matrices[0].shape

    T = np.zeros((x_shape, y_shape, z_shape * len(distros_matrices)))

    for i, j, k, (l, distro_matrix) in product(
        range(x_shape),
        range(y_shape),
        range(z_shape),
        enumerate(distros_matrices),
    ):
        T[i][j][k + z_shape * l] = distro_matrix[i][j][k]
    return T


def sum_distros_matrices(distros_matrices: list):
    """
    let X[i][j] and Y[i][j] two distribution matrices for two different
    signals but for the same channel, where i is the index of mass and j is
    the index of gu. Each entry is a distribution of X[i][j]. This function
    returns a new matrix T[i][j] = X[i][j] + Y[i][j] + ....
    """
    x_shape, y_shape, z_shape = distros_matrices[0].shape

    T = np.zeros((x_shape, y_shape, z_shape))

    for i, j, k, (l, distro_matrix) in product(
        range(x_shape),
        range(y_shape),
        range(z_shape),
        enumerate(distros_matrices),
    ):
        T[i][j][k] += distro_matrix[i][j][k]
    return T


def get_concatenated_signal_distros(
    channels, signal_groups, masses, gu_values, case
):
    signals = signal_groups.keys()
    distros_matrices_by_channel = {
        channel: get_signal_channel_distros(
            channel, signal_groups, masses, gu_values, case
        )
        for channel in channels
    }
    concatenated_distros = {}
    for signal in signals:
        distros_matrices = [
            distros_matrices_by_channel[channel][signal]
            for channel in channels
        ]
        concatenated_distros[signal] = concatenate_distros_matrices(
            distros_matrices
        )
    combined_distros = sum_distros_matrices(
        list(concatenated_distros.values())
    )
    concatenated_distros["combined"] = combined_distros

    return concatenated_distros


def get_concatenated_bkg_distros(channels, distros_matrices_by_channel, keys):
    signals = keys

    concatenated_distros = {}
    for signal in signals:
        distros_matrices = [
            distros_matrices_by_channel[channel][signal]
            for channel in channels
        ]
        concatenated_distros[signal] = concatenate_distros_matrices(
            distros_matrices
        )
    combined_distros = sum_distros_matrices(
        list(concatenated_distros.values())
    )
    concatenated_distros["combined"] = combined_distros

    return concatenated_distros


def calculate_significance(case, signal, masses, gu_values):
    signal_final_distros = get_concatenated_signal_distros(
        channels, signal_groups, masses, gu_values, case
    )
    bkg_distros_by_channel = {
        channel: {
            key: get_xgb_matrix(
                value,
                channel,
                case,
                XGB_distros_path,
                masses,
                gu_values,
                integral=get_bkg_events(channel, bkg_groups)[key],
            )
            for key, value in bkg_name.items()
        }
        for channel in channels
    }
    bkg_final_distros = get_concatenated_bkg_distros(
        channels, bkg_distros_by_channel, bkg_name.keys()
    )
    significances_matrix = np.zeros((len(masses), len(gu_values)))
    for (i, mass), (j, gu) in product(enumerate(masses), enumerate(gu_values)):
        significances_matrix[i][j] = approx_global_sig(
            signal_final_distros[signal][i][j],
            bkg_final_distros["combined"][i][j],
        )
    return significances_matrix


print(TEMP_DIR)

# calculate cross sections matrices
# gen_xs_matrices(cases, signal_production_channels)

# Run Full Simulations with preselections wuth gu fixed, gu = 1.

# Parton level kinematic distributions

# Hadr. level kinematic distributions

# Cut flow tables

# Calculate number of events physical events that pass the cuts

# Run ML Algorithms

# ML output distributions
import numpy as np

masses = np.arange(lower_mass, upper_mass + mass_step, mass_step)
gu_values = np.arange(lower_g_u, upper_g_u + g_u_step, g_u_step)

bkg_name = {
    "ttbar": "tbart",
    "Vjets": "V+jets",
    "VV": "Diboson",
    "single_top": "stop",
}

# get_signal_events(channel, signal_groups, 500, 1, case)

# signal_channel_distros = get_signal_channel_distros(
#     channel, signal_groups, masses, gu_values, case
# )

# print(signal_channel_distros["non-res"][0][1].sum())
# channel = channels[0]
# bkg_channel_distros = {
#     key: get_xgb_matrix(
#         value,
#         channel,
#         case,
#         XGB_distros_path,
#         masses,
#         gu_values,
#         integral=get_bkg_events(channel, bkg_groups)[key],
#     )
#     for key, value in bkg_name.items()
# }
# print(bkg_channel_distros["ttbar"][1][1].sum())

# Calculate Significances and Limits
case = "wRHC"
signal_list = ["non-res", "sLQ", "dLQ", "combined"]
significances = {
    signal: calculate_significance(case, signal, masses, gu_values)
    for signal in signal_list
}
# Delete temp dir
shutil.rmtree(TEMP_DIR)

import matplotlib.pyplot as plt
import pandas as pd

from hep_pheno_tools.analysis_tools.heatmaps_tools import plot_heatmap, smooth


def Calcular_g_U(c_U, M):
    v = 246
    return 2 * np.sqrt(c_U) * M * 1000 / v


signal = "combined"


def get_curves(signal):
    matrix = significances[signal]
    masses_in_text = [mass / 1000 for mass in masses]
    gu_values_in_text = [gu for gu in gu_values]
    df = pd.DataFrame(
        matrix * 0.78, index=masses_in_text, columns=gu_values_in_text
    ).T
    Data_Interpolate = smooth(df, log=True)

    if case == "wRHC":
        c_u1, c_u2 = 0.006, 0.002
    else:
        c_u1, c_u2 = 0.017, 0.007
    fig, ax, curves = plot_heatmap(
        Data_Interpolate,
        level_curves={
            np.log10(1.69): r"$1.69 \sigma$",
            np.log10(3): r"$3 \sigma$",
            np.log10(5): r"$5 \sigma$",
        },
        level_curves_labels_locations=[
            [1400 / 1000, 2],
            [1550 / 1000, 2],
            [1650 / 1000, 2],
        ],
        x_label=r"$M_{U}$ [TeV]",
        y_label=r"$g_U$",
        cbar_label=r"$\log_{10}$(Significance)",
    )
    x_min = 1  # TeV
    x_max = 3.50  # TeV
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(0.5, 3.5)
    x = np.linspace(x_min, x_max, 100)
    x_1, y_1 = x_min, Calcular_g_U(c_u1, x_min)
    x_2, y_2 = x_max, Calcular_g_U(c_u1, x_max)

    x_3, y_3 = x_min, Calcular_g_U(c_u2, x_min)
    x_4, y_4 = x_max, Calcular_g_U(c_u2, x_max)

    y1 = np.poly1d(np.polyfit([x_1, x_2], [y_1, y_2], deg=1))(x)
    y2 = np.poly1d(np.polyfit([x_3, x_4], [y_3, y_4], deg=1))(x)

    ax.plot(x, y1, c="black", alpha=0.5)
    ax.plot(x, y2, c="black", alpha=0.5)

    x = np.concatenate((x[0], x, x[-1]), axis=None)
    y = np.concatenate((y2[0], y1, y2[-1]), axis=None)

    ax.fill(x, y, "gray", alpha=0.3, label=r"$1 \sigma R_{D^{(*)}}$")
    plt.legend(fontsize=12, framealpha=0.4)
    plt.title(
        r"$\mathbf{\sqrt{s}}$ = 13 TeV, L = 137 $\mathbf{fb^{-1}}$ $\beta$",
        loc="right",
        fontsize=12,
        fontweight="bold",
    )
    return curves


import pickle

for signal in ["non-res", "sLQ", "dLQ", "combined"]:
    curves = get_curves(signal)
    path = os.path.join(DATA_DIR, "significances_curves", case, signal)
    os.makedirs(path, exist_ok=True)
    with open(os.path.join(path, "curves.pkl"), "wb") as f:
        pickle.dump(curves, f)
