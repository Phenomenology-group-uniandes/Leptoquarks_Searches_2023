import os
import multiprocessing as mp

from hep_pheno_tools.madgraph_tools import get_seeds_from_mg5_output_folder
from hep_pheno_tools.madgraph_tools import get_new_seed
from hep_pheno_tools.madgraph_tools import run_mg5

from .convert_matrices_to_params_dict import model_parameters
from .generate_outputs import generate_param_cards
from .generate_outputs import generate_mg5_output_script


def get_xs(
        mass,
        g,
        param_cards_folder_path: str,
        temp_dir: str,
        kin_gen_cuts: dict,
        channel: str = "non-res",
        case: str = "woRHC",
        n_events: int = 10000,
        n_workers: int = mp.cpu_count()
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
