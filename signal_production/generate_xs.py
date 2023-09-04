import os
import tempfile
from . import convert_matrices_to_params_dict as cmpd
from ..hep_pheno_tools.madgraph_tools import run_mg5
from ..hep_pheno_tools.madgraph_tools import get_new_seed
from ..hep_pheno_tools.madgraph_tools import get_seed_from_banner
from ..hep_pheno_tools.madgraph_tools import get_seeds_from_mg5_output_folder

current_file_path = os.path.abspath(__file__)
parent_directory_path = os.path.dirname(current_file_path)
model_directory_path = os.path.join(
    os.path.dirname(parent_directory_path), "model"
    )
mod2_vlq_ufo_path = os.path.join(model_directory_path, "Mod2_VLQ_UFO")

if not os.path.exists(mod2_vlq_ufo_path):

    raise FileNotFoundError(
        f"Path to Mod2_VLQ_UFO not found: {mod2_vlq_ufo_path}"
        )


decay_modes = f"""
import model {mod2_vlq_ufo_path}
generate vlq > all all
add process zp > all all
"""


def generate_param_cards(
        mass,
        gu,
        param_card_dir: str,
        model_parameters: dict,
        temp_dir: str,
        seeds: list,
        n_events: int = 1000,
        ):
    mg5_output_folder = tempfile.mkdtemp(dir=temp_dir)
    os.makedirs(mg5_output_folder, exist_ok=True)
    param_card_dict = cmpd(model_parameters)

    # Write mg5 script with decay modes
    f = open(os.path.join(mg5_output_folder, "calculate_decay_width.mg5"), "w")
    f.write(decay_modes)
    f.write(f"output {mg5_output_folder} -nojpeg\n")
    f.close()
    run_mg5(os.path.join(mg5_output_folder, "calculate_decay_width.mg5"))

    # Write me script to calculate decay width
    f = open(os.path.join(mg5_output_folder, "calculate_decay_width.me"), "w")
    f.write(f"launch {mg5_output_folder} -i\n")
    f.write("calculate_decay_widths\n")
    seed = get_new_seed(seeds)
    # set run_card
    f.write(f"set iseed {seed}\n")
    f.write(f"set nevents {n_events}\n")
    # set param_card
    f.write(f"set MVLQ {mass}\n")
    f.write(f"set GU {gu}\n")
    [f.write(f"set {key} {value}\n") for key, value in param_card_dict.items()]
    f.write("exit\n")
    f.close()
    run_mg5(os.path.join(mg5_output_folder, "calculate_decay_width.me"))

    # Copy param_card.dat into param_cards_path
    source = os.path.join(
        mg5_output_folder,
        "Events",
        "run_01",
        "param_card.dat"
        )
    if not os.path.exists(source):
        os.rmdir(mg5_output_folder)
        raise FileNotFoundError(f"Path to param_card.dat not found: {source}")
    target = os.path.join(param_card_dir, "param_card.dat")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    os.rename(source, target)
    # Clear temp dir
    os.rmdir(mg5_output_folder)


def generate_xs(
        mass,
        g,
        param_cards_path: str,
        model_parameters: dict,
        temp_dir: str,
        mod2_vlq_ufo_path: str = mod2_vlq_ufo_path,
        ):
    cmpd(model_parameters)
    pass
