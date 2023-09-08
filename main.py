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
mass_step = 125
lower_g_u = 0.5
upper_g_u = 3.5
g_u_step = 0.25
parton_n_events = 20000

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


@timer
def gen_csv_matrices(cases, channels):
    print("Generating cross section matrices...")
    with mp.Pool() as pool:
        pool.map(
            gen_csv_matrix,
            product(cases, channels)
        )


if __name__ == "__main__":
    print(TEMP_DIR)

    # calculate cross sections matrices
    gen_csv_matrices(cases, channels)

    # Run Full Simulations with preselections

    # Parton level kinematic distributions

    # Hadr. level kinematic distributions

    # Cut flow tables

    # Preselection efficiency matrices

    # N Events on preselection

    # Run ML Algorithms

    # ML output distributions

    # Normalize ML output distributions

    # Calculate Significances and Limits

    # Delete temp dir
    shutil.rmtree(TEMP_DIR)
