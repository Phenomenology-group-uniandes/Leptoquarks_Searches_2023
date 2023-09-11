import os
from itertools import product

import numpy as np


# Matrix of Distributions, I use the gu=1 distro for all gu values
def get_xgb_matrix(
    channel_name,
    selection_channel,
    case,
    XGB_distros_path,
    masses,
    gu_values,
    integral=1,
):
    xgb_distro_gu1 = np.loadtxt(
        os.path.join(
            XGB_distros_path,
            case,
            "M1250",
            selection_channel,
            f"high_per_bin_{channel_name}.txt",
        )
    )
    n_bins = len(xgb_distro_gu1)
    xgb_matrix = np.zeros((len(masses), len(gu_values), n_bins))
    for i, mass in enumerate(masses):
        if mass < 1000:
            m = 1000
        elif mass > 2500:
            m = 2500
        else:
            m = mass
        xgb_distro_gu1 = np.loadtxt(
            os.path.join(
                XGB_distros_path,
                case,
                f"M{m}",
                selection_channel,
                f"high_per_bin_{channel_name}.txt",
            )
        )
        xgb_distro_gu1 = xgb_distro_gu1 * integral / sum(xgb_distro_gu1)
        for (j, _), (k, bin_content) in product(
            enumerate(gu_values), enumerate(xgb_distro_gu1)
        ):
            xgb_matrix[i, j, k] = bin_content
    return xgb_matrix
