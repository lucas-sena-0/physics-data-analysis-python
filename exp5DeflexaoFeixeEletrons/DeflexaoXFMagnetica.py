import matplotlib.pyplot as plt
import numpy as np


#DeflexaoXFMagnetica
 
# Dados de corrente e deflexão
I300 = np.array([0.001, 0.376, 0.797, 1.171, 1.532, 1.984, 2.443, 2.795, 3.183, 3.6, 3.815])
D300 = np.array([0, 0.3, 0.7, 1, 1.35, 1.75, 2.25, 2.65, 3.1, 3.5, 3.8])

I400 = np.array([0.006, 0.347, 0.801, 1.212, 1.551, 1.927, 2.365, 2.788, 3.176, 3.567, 3.824])
D400 = np.array([0, 0.2, 0.55, 0.75, 1.1, 1.4, 1.7, 2.1, 2.4, 2.7, 2.95])

I500 = np.array([0.009, 0.443, 0.838, 1.233, 1.609, 2.004, 2.433, 2.794, 3.212 , 3.575, 3.953])
D500 = np.array([0, 0.35, 0.5, 0.8, 1.05, 1.3, 1.6, 1.9, 2.3, 2.6, 2.9])

I600 = np.array([0.009, 0.425, 0.811, 1.224, 1.650, 2.001, 2.446, 2.810, 3.190, 3.628, 3.994])
D600 = np.array([0, 0.2, 0.4, 0.9, 1.0, 1.2, 1.5, 1.8, 2.1, 2.4, 2.6])

# Pontos de calibração: I -> B (mT)
I_cal = np.array([1.053, 2.122, 3.018])
B_cal_mT = np.array([0.2, 0.33, 0.45])

# Ajuste linear: B = a*I + b
a, b = np.polyfit(I_cal, B_cal_mT, 1)

def B_est(I):
    return a * I + b

# Estimativa de B para cada série
B300 = B_est(I300)
B400 = B_est(I400)
B500 = B_est(I500)
B600 = B_est(I600)

# Plot
plt.figure(figsize=(9,6))
plt.plot(B300, D300, 'o-', label='300 V')
plt.plot(B400, D400, 's-', label='400 V')
plt.plot(B500, D500, 'd-', label='500 V')
plt.plot(B600, D600, '^-', label='600 V')

plt.xlabel("Força Magnética B (mT)", fontsize=12)
plt.ylabel("Deflexão do Feixe (cm)", fontsize=12)
plt.title("Deflexão do Feixe em Função da Força Magnética", fontsize=14)
plt.grid(True)
plt.legend()
plt.show()
