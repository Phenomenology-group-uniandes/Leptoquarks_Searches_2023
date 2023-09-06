import os
import shutil
import subprocess
import tempfile
from signal_production.get_xs import (
    get_xs
    )

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

# Delete all the temp folders
[shutil.rmtree(f) for f in os.listdir(os.getcwd()) if "tmp" in f]

# Create a temporary directory
TEMP_DIR = tempfile.mkdtemp(dir=os.getcwd())
PARAMS_DIR = os.path.join(os.getcwd(), "data", "Pararamcards")
# Define the kinematic generation cuts
parton_kin_gen_cuts = {
    "cut_decays": True,
    "ptb": 30,
    "ptj": 20,
    "ptl": 20,
    "etab": 2.5,
    "pt_min_pdg": "{15: 30}",
    "eta_max_pdg": '{15: 2.5}',
    'mxx_min_pdg': '{15:100}'
}


if __name__ == "__main__":
    print(TEMP_DIR)
    get_xs(
        mass=1000,
        g=1,
        param_cards_folder_path=PARAMS_DIR,
        temp_dir=TEMP_DIR,
        kin_gen_cuts=parton_kin_gen_cuts,
        channel="non-res",
        case="woRHC",
        n_events=1000,
        n_workers=3
        )
    # delete temp dir
    shutil.rmtree(TEMP_DIR)
