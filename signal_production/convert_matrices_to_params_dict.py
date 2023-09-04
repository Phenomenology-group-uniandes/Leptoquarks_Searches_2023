import numpy as np
# Model parameters
model_parameters = {}
model_parameters["woRHC"] = {
  "beta_matrix_l": np.array([
      [0, 0, None],
      [0, 0, 0],
      [0, 0, 1]
  ]),
  "beta_matrix_r": np.diag([0, 0, 0]),
  "zeta_matrix_l": np.array([
      [0, 0, 0],
      [0, 0, 0],
      [0, 0, 1]
  ]),
  "zeta_matrix_e_r": np.diag([0, 0, 0]),
  "zeta_matrix_q_l": np.diag([0, 0, 1]),
  "zeta_matrix_u_r": np.diag([0, 0, 0]),
  "zeta_matrix_d_r": np.diag([0, 0, 0]),
  "kappau": 0,
  "kappautilde": 0,
  "kappazp": 0
}

# wRHC = woRHC with beta_matrix_r = diag(0, 0, -1)
model_parameters["wRHC"] = model_parameters["woRHC"].copy()
model_parameters["wRHC"]["beta_matrix_r"] = np.diag([0, 0, -1])


def convert_matrices_to_params_dict(lq_matrices):
    m_dict = lq_matrices
    params = {}

    # pass beta_matrix_l to params
    params["BETAL33"] = m_dict["beta_matrix_l"][2, 2]
    params["BETAL23"] = m_dict["beta_matrix_l"][1, 2]
    params["BETAL32"] = m_dict["beta_matrix_l"][2, 1]

    # pass beta_matrix_r to params
    params["BETARD33"] = m_dict["beta_matrix_r"][2, 2]

    # pass zeta_matrix_l to params
    params["ZETAL33"] = m_dict["zeta_matrix_l"][2, 2]
    params["ZETAL23"] = m_dict["zeta_matrix_l"][1, 2]
    params["ZETAL22"] = m_dict["zeta_matrix_l"][1, 1]

    herm = m_dict["zeta_matrix_l"] == m_dict["zeta_matrix_l"].conj().T
    if not herm.all():
        raise Exception("zeta_matrix_l is not herm")

    # pass zeta_matrix_e_r to params
    params["ZETARE33"] = m_dict["zeta_matrix_e_r"][2, 2]
    params["ZETARE22"] = m_dict["zeta_matrix_e_r"][1, 1]

    herm = m_dict["zeta_matrix_e_r"] == m_dict["zeta_matrix_e_r"].conj().T

    if not herm.all():
        raise Exception("zeta_matrix_e_r is not herm")

    # pass zeta_matrix_q_l to params
    params["ZETAQ33"] = m_dict["zeta_matrix_q_l"][2, 2]
    params["ZETAQLL"] = m_dict["zeta_matrix_q_l"][1, 1]

    herm = m_dict["zeta_matrix_q_l"] == m_dict["zeta_matrix_q_l"].conj().T
    A = m_dict["zeta_matrix_q_l"][1, 1]
    B = m_dict["zeta_matrix_q_l"][0, 0]
    is_block_diagonal = A == B

    if not herm.all():
        raise Exception("zeta_matrix_q_l is not herm")
    elif not is_block_diagonal:
        raise Exception("zeta_matrix_q_l is not block diagonal")

    # pass zeta_matrix_u_r to params
    params["ZETARU33"] = m_dict["zeta_matrix_u_r"][2, 2]
    params["ZETARULL"] = m_dict["zeta_matrix_u_r"][1, 1]

    herm = m_dict["zeta_matrix_u_r"] == m_dict["zeta_matrix_u_r"].conj().T
    A = m_dict["zeta_matrix_u_r"][1, 1]
    B = m_dict["zeta_matrix_u_r"][0, 0]
    is_block_diagonal = A == B

    if not herm.all():
        raise Exception("zeta_matrix_u_r is not herm")
    elif not is_block_diagonal:
        raise Exception("zeta_matrix_u_r is not block diagonal")

    # pass zeta_matrix_d_r to params

    params["ZETARD33"] = m_dict["zeta_matrix_d_r"][2, 2]
    params["ZETARDLL"] = m_dict["zeta_matrix_d_r"][1, 1]

    herm = m_dict["zeta_matrix_d_r"] == m_dict["zeta_matrix_d_r"].conj().T
    A = m_dict["zeta_matrix_d_r"][1, 1]
    B = m_dict["zeta_matrix_d_r"][0, 0]
    is_block_diagonal = A == B

    if not herm.all():
        raise Exception("zeta_matrix_d_r is not herm")
    elif not is_block_diagonal:
        raise Exception("zeta_matrix_d_r is not block diagonal")

    # pass kappau to params
    params["KAPPAU"] = m_dict["kappau"]
    params["KAPPAUTILDE"] = m_dict["kappautilde"]

    # pass kappazp to params
    params["KAPPAZP"] = m_dict["kappazp"]
    return params
