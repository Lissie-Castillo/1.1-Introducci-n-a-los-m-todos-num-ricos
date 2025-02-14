#   Codigo que implementa un esquema numerico 
#   para determinar la aproximacion de Leibniz
# 
#           Autor:
#   Dr. Ivan de Jesus May-Cen
#   imaycen@hotmail.com
#   Version 1.0 : 29/01/2025
#

import numpy as np
import matplotlib.pyplot as plt

def leibniz_pi(n):
    return 4 * sum((-1)**k / (2*k + 1) for k in range(n))

true_pi = np.pi
N_values = [10, 100, 1000, 10000]
errors_abs = []
errors_rel = []
errors_cua = []

for N in N_values:
    approx_pi = leibniz_pi(N)
    error_abs = abs(true_pi - approx_pi)
    error_rel = error_abs / true_pi
    error_cua = error_abs**2
    errors_abs.append(error_abs)
    errors_rel.append(error_rel)
    errors_cua.append(error_cua)
    print(f"N={N}: Error absoluto={error_abs}, Error relativo={error_rel},Error cuadrático={error_cua}")

plt.figure()
plt.plot(N_values, errors_abs, label='Error absoluto', marker='o')
plt.plot(N_values, errors_rel, label='Error relativo', marker='s')
plt.plot(N_values, errors_cua, label='Error cuadrático', marker='^')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N')
plt.ylabel('Error')
plt.legend()
plt.title('Errores en la aproximación de pi')
plt.show()