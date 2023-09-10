import os
import time
import shutil
import subprocess
from itertools import product
import multiprocessing as mp
import tempfile

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
channels = [
    "non-res",
    "sLQ",
    "dLQ"
    ]

lower_mass = 500
upper_mass = 5000
mass_step = 250
lower_g_u = 0.5
upper_g_u = 3.5
g_u_step = 0.25
parton_n_events = 30000

n_workers = 2


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
        n_workers=int(mp.cpu_count()/n_workers)
    )
    csv_path = os.path.join(
        DATA_DIR,
        "cross_sections",
        case,
        channel,
        "xs_matrix.csv"
    )
    os.makedirs(os.path.dirname(csv_path), exist_ok=True)
    xs_matrix.to_csv(csv_path)
    xs_matrix.to_excel(csv_path.replace(".csv", ".xlsx"))


@timer
def gen_xs_matrices(cases, channels):
    print("Generating cross section matrices...")
    with mp.Pool() as pool:
        pool.map(
            gen_csv_matrix,
            product(cases, channels)
        )
    pass


# Matrix of Distributions, I use the gu=1 distro for all gu values
def get_xgb_matrix(channel_name, case):
    xgb_distro_gu1 = np.loadtxt(
        os.path.join(
            XGB_distros_path,
            case,
            "M1000",
            f"high_per_bin_{channel_name}.txt"
        )
    )
    n_bins = len(xgb_distro_gu1)
    xgb_matrix = np.zeros((len(masses), len(gu_values), n_bins))
    for i, mass in enumerate(masses):
        if mass < 1000:
            m = 1000
        elif mass > 2500:
            m = 2500
        else:
            m = mass
        xgb_distro_gu1 = np.loadtxt(
            os.path.join(
                XGB_distros_path,
                case,
                f"M{m}",
                f"high_per_bin_{channel_name}.txt"
            )
        )
        xgb_distro_gu1 = xgb_distro_gu1 / sum(xgb_distro_gu1)
        for (j, gu), (k, bin_content) in product(
            enumerate(gu_values),
            enumerate(xgb_distro_gu1)
        ):
            xgb_matrix[i, j, k] = bin_content
    return xgb_matrix


if __name__ == "__main__":
    print(TEMP_DIR)

    # calculate cross sections matrices
    # gen_xs_matrices(cases, channels)

    # Run Full Simulations with preselections wuth gu fixed, gu = 1.

    # Parton level kinematic distributions

    # Hadr. level kinematic distributions

    # Cut flow tables

    # Preselection efficiency matrices

    # N Events on preselection

    # Run ML Algorithms
    XGB_distros_path = os.path.join(DATA_DIR, "XGB_distros")

    # ML output distributions
    import numpy as np
    masses = np.arange(lower_mass, upper_mass+mass_step, mass_step)
    gu_values = np.arange(lower_g_u, upper_g_u+g_u_step, g_u_step)
    signal_channel_name = {
        "non-res": "tau_tau",
        "sLQ": "tau_Lq",
        "dLQ": "Lq_Lq",
        "combined": "Combined"
    }
    bkg_channel_name = {
        'ttbar': 'tbart',
        'Vjets': 'V+jets',
        'VV': 'Diboson',
        'single_top': 'Single top',
    }

    signal_channel_distros = {
        key: get_xgb_matrix(value, "wRHC")
        for key, value in signal_channel_name.items()
        }

    # Normalize ML output distributions

    # Calculate Significances and Limits

    # Delete temp dir
    shutil.rmtree(TEMP_DIR)
