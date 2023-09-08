import os
import shutil
import tempfile
import multiprocessing as mp
from io import StringIO

import pandas as pd

from hep_pheno_tools.madgraph_tools import get_seeds_from_mg5_output_folder
from hep_pheno_tools.madgraph_tools import get_new_seed
from hep_pheno_tools.madgraph_tools import run_mg5

from .generate_outputs import generate_mg5_output_script
from .generate_outputs import get_param_card_file_path


def get_xs(
        mass: float,
        g: float,
        param_cards_folder_path: str,
        temp_dir: str,
        kin_gen_cuts: dict,
        channel: str = "non-res",
        case: str = "woRHC",
        n_events: int = 10000,
        n_workers: int = mp.cpu_count()
        ):

    paramcard_path = get_param_card_file_path(
        mass,
        g,
        param_cards_folder_path,
        temp_dir,
        case,
        n_events/5
        )

    mg5_output_folder = tempfile.mkdtemp(dir=temp_dir)

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

    with open(os.path.join(mg5_output_folder, "crossx.html"), 'r') as f:
        html_string = f.read()

    t = pd.read_html(StringIO(html_string))[0]
    try:
        xs = float(t['Cross section (pb)'][0].split(" ")[0])
    except ValueError:
        xs = 0.0

    # clean mg5_output_folder
    shutil.rmtree(mg5_output_folder)
    return xs
