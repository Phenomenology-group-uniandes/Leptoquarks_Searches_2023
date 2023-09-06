import numpy as np
import pandas as pd
import multiprocessing as mp
import itertools
from .get_xs import get_xs


def get_xs_matrix(
        param_cards_folder_path: str,
        temp_dir: str,
        kin_gen_cuts: dict,
        lower_mass: float = 1000,
        upper_mass: float = 3500,
        mass_step: float = 125,
        lower_g_u: float = 0.5,
        upper_g_u: float = 2.0,
        g_u_step: float = 0.25,
        case: str = "woRHC",
        channel: str = "non-res",
        n_events: int = 10000,
        n_workers: int = mp.cpu_count(),
        test: bool = False
        ):
    # Leptoquark parameters
    M_U = np.arange(lower_mass, upper_mass + mass_step, mass_step)
    g_U = np.arange(lower_g_u, upper_g_u + g_u_step, g_u_step)
    if test:
        M_U = np.array([1000, 1250])
        g_U = np.array([1.0, 1.75])
    xs_matrix = pd.DataFrame(index=g_U, columns=M_U)
    for m, g in itertools.product(M_U, g_U):
        xs = get_xs(
            mass=m,
            g=g,
            param_cards_folder_path=param_cards_folder_path,
            temp_dir=temp_dir,
            kin_gen_cuts=kin_gen_cuts,
            channel=channel,
            case=case,
            n_events=n_events,
            n_workers=n_workers
            )
        xs_matrix[m][g] = xs
    return xs_matrix
