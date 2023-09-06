import os
import shutil
import tempfile
from .convert_matrices_to_params_dict import model_parameters
from .convert_matrices_to_params_dict import convert_matrices_to_params_dict
from hep_pheno_tools.madgraph_tools import get_seeds_from_mg5_output_folder
from hep_pheno_tools.madgraph_tools import get_new_seed
from hep_pheno_tools.madgraph_tools import run_mg5

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


decay_modes_headers = f"""
import model {mod2_vlq_ufo_path}
generate vlq > all all
add process zp > all all
"""
tau_tau_header = f"""
import model {mod2_vlq_ufo_path}
generate p p > ta+ ta- / zp QED=0 QCD=0
"""
headers = {
    "decay_modes": decay_modes_headers,
    "non-res": tau_tau_header
}

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


def generate_param_cards(
        mass,
        gu,
        param_card_dir: str,
        model_parameters: dict,
        temp_dir: str,
        seeds: list,
        n_events: int = 1000,
        gzp=0,
        ):
    mg5_output_folder = tempfile.mkdtemp(dir=temp_dir)
    os.makedirs(mg5_output_folder, exist_ok=True)
    param_card_dict = convert_matrices_to_params_dict(model_parameters)

    # Write mg5 script with decay modes
    f = open(os.path.join(mg5_output_folder, "calculate_decay_width.mg5"), "w")
    f.write(headers["decay_modes"])
    f.write(f"output {mg5_output_folder} -nojpeg\n")
    f.close()
    run_mg5(os.path.join(mg5_output_folder, "calculate_decay_width.mg5"))

    # Write me script to calculate decay width
    f = open(os.path.join(mg5_output_folder, "calculate_decay_width.me"), "w")
    # f.write(f"launch {mg5_output_folder} -i\n")
    f.write("calculate_decay_widths\n")
    seed = get_new_seed(seeds)
    # set run_card
    f.write(f"set iseed {seed}\n")
    f.write(f"set nevents {n_events}\n")
    # set param_card
    f.write(f"set MVLQ {mass}\n")
    f.write(f"set GU {gu}\n")
    f.write(f"set GZP {gzp}\n")
    [f.write(f"set {key} {value}\n") for key, value in param_card_dict.items()]
    f.write("exit\n")
    f.close()
    run_mg5(
        os.path.join(mg5_output_folder, "calculate_decay_width.me"),
        MG5_PATH=os.path.join(mg5_output_folder, "bin", "madevent"),
        )

    # Copy param_card.dat into param_cards_path
    source = os.path.join(
        mg5_output_folder,
        "Events",
        "run_01",
        "param_card.dat"
        )
    if not os.path.exists(source):
        raise FileNotFoundError(f"Path to param_card.dat not found: {source}")
    target = os.path.join(param_card_dir, "param_card.dat")
    os.makedirs(os.path.dirname(target), exist_ok=True)
    os.rename(source, target)
    # Clear temp dir
    shutil.rmtree(mg5_output_folder)


def generate_mg5_output_script(
        mg5_output_folder: str,
        channel: str = "tau_tau"
        ):
    script_path = os.path.join(mg5_output_folder, "generate_mg5_output.mg5")
    # Write mg5 script with production mode
    f = open(script_path, "w")
    f.write(headers[channel])
    f.write(f"output {mg5_output_folder} -nojpeg\n")
    f.close()
    run_mg5(script_path)
    return mg5_output_folder


def launch_mg5(
        mass,
        g,
        param_cards_folder_path: str,
        temp_dir: str,
        channel: str = "non-res",
        case: str = "woRHC",
        n_events: int = 10000,
        n_workers: int = 3,
        kin_gen_cuts: dict = parton_kin_gen_cuts
        ):

    paramcard_path = os.path.join(
        param_cards_folder_path,
        f"MU{int(mass)}",
        f"GU{g}".replace(".", "_"),
        "param_card.dat"
        )
    if not os.path.exists(paramcard_path):
        generate_param_cards(
            mass,
            g,
            param_card_dir=os.path.dirname(paramcard_path),
            model_parameters=model_parameters[case],
            temp_dir=temp_dir,
            seeds=list(),
            n_events=int(n_events/10)
            )
    mg5_output_folder = os.path.join(
        temp_dir,
        case,
        channel,
        str(mass),
        str(g)
        )
    os.makedirs(mg5_output_folder, exist_ok=True)

    # check if mg5_output_folder is empty
    if not os.listdir(mg5_output_folder):
        generate_mg5_output_script(
            mg5_output_folder=mg5_output_folder,
            channel=channel
            )
    # Write me script to launch mg5
    f = open(os.path.join(mg5_output_folder, "generate_events.mg5"), "w")
    f.write(f"launch {mg5_output_folder} -m\n")
    f.write(f"{n_workers}\ndone\n")
    seed = get_new_seed(get_seeds_from_mg5_output_folder(mg5_output_folder))
    f.write(f"set iseed {seed}\n")
    f.write(f"set nevents {n_events}\n")
    f.write('set sde_strategy 1\n')
    [f.write(f"set {cut} {kin_gen_cuts[cut]}\n") for cut in kin_gen_cuts]
    f.write(f"{paramcard_path}\n")
    f.write("exit\n")
    f.close()
    run_mg5(os.path.join(mg5_output_folder, "generate_events.mg5"))
