import os
import subprocess
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


# Global variables

TEMP_DIR = tempfile.mkdtemp()



def run_mg5(scriptfile: str, MG5_PATH: str = MG5_PATH) -> subprocess.Popen:
    if not os.path.exists(MG5_PATH):
        raise FileNotFoundError(f"Path to MG5 not found: {MG5_PATH}")
    if not os.path.exists(scriptfile):
        raise FileNotFoundError(f"Path to scriptfile not found: {scriptfile}")

    return subprocess.Popen(
        [MG5_PATH, scriptfile],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        stdin=subprocess.PIPE,
        )


if __name__ == "__main__":
    print(TEMP_DIR)
    # delete temp dir
    os.rmdir(TEMP_DIR)

