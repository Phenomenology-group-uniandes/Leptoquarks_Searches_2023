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


# Create a temporary directory inside the framework
TEMP_DIR = tempfile.mkdtemp(dir=hep_pheno_tools.__path__[0])


if __name__ == "__main__":
    print(TEMP_DIR)
    # delete temp dir
    os.rmdir(TEMP_DIR)
