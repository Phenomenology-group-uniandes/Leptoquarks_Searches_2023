import os
import multiprocessing as mp

from hep_pheno_tools.madgraph_tools import get_seeds_from_mg5_output_folder
from hep_pheno_tools.madgraph_tools import get_new_seed
from hep_pheno_tools.madgraph_tools import run_mg5

from .generate_outputs import generate_mg5_output_script
from .generate_outputs import get_param_card_file_path


def launch_fullsim(
    mass: float,
    g: float,
    param_cards_folder_path: str,
    pythia_card_path: str,
    delphes_card_path: str,
    temp_dir: str,
    kin_gen_cuts: dict,
    data_dir: str,
    channel: str = "non-res",
    case: str = "woRHC",
    n_events: int = 50000,
    n_workers: int = mp.cpu_count(),
):
    paramcard_path = get_param_card_file_path(
        mass, g, param_cards_folder_path, temp_dir, case, n_events / 50
    )

    mg5_output = os.path.join(temp_dir, channel, case, f"mg5_{mass}_{g}")
    os.makedirs(mg5_output, exist_ok=True)
    data_output = os.path.join(
        data_dir,
        f"MU{mass}",
        f"GU{g}",
        case,
        channel,
    )
    os.makedirs(data_output, exist_ok=True)

    # check if mg5_output_folder is empty
    if not os.listdir(mg5_output):
        generate_mg5_output_script(
            mg5_output_folder=mg5_output, channel=channel
        )
    # get seeds used
    seeds = get_seeds_from_mg5_output_folder(data_output)
    seed = get_new_seed(seeds)
    # Write script to launch mg5 with pythia8 and delphes
    f = open(os.path.join(mg5_output, "generate_events.mg5"), "w")
    f.write(f"launch {mg5_output} -m\n")
    f.write(f"{n_workers}\ndone\n")
    f.write("SHOWER=Pythia8\n")
    f.write("DETECTOR=Delphes\n")
    f.write("done\n")
    # set run_card
    f.write(f"set iseed {seed}\n")
    f.write(f"set nevents {n_events}\n")
    f.write("set sde_strategy 1\n")
    [f.write(f"set {cut} {kin_gen_cuts[cut]}\n") for cut in kin_gen_cuts]
    # set param_card, pythia_card, and delphes_card
    f.write(f"{paramcard_path}\n")
    f.write(f"{pythia_card_path}\n")
    f.write(f"{delphes_card_path}\n")
    f.write("exit\n")
    f.close()
    run_mg5(os.path.join(mg5_output, "generate_events.mg5"))
    return mg5_output, data_output
