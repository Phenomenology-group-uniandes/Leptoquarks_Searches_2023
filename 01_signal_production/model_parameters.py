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
