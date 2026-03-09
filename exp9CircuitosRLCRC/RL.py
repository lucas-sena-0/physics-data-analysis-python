import numpy as np
import pandas as pd

# Dados fornecidos
frequencias = np.array([315, 4617, 10000])  # Hz
R = 100  # ohms
L = 44e-3  # henrys
V_R_exp = np.array([9.7, 9.9, 3.88])  # V
V_L_exp = np.array([0.95, 0.752, 9.5])  # V

# Cálculo da corrente na malha
I = V_R_exp / R  # Corrente (A)

# Reatância indutiva
X_L = 2 * np.pi * frequencias * L

# Impedância total
Z = np.sqrt(R**2 + X_L**2)

# Ângulo de fase (em graus)
phi = np.arctan(X_L / R) * (180 / np.pi)

# Tensão teórica no indutor
V_L_teo = I * X_L

# Erro relativo da tensão no indutor (%)
erro_V_L = (V_L_teo - V_L_exp) / V_L_exp * 100

# Tabela de resultados
df = pd.DataFrame({
    "Frequência (Hz)": frequencias,
    "Corrente (A)": I,
    "X_L (ohms)": X_L,
    "|Z| (ohms)": Z,
    "Fase (°)": phi,
    "V_L teórico (V)": V_L_teo,
    "V_L exp (V)": V_L_exp,
    "Erro V_L (%)": erro_V_L
})

# Arredondar para melhor visualização
df = df.round({
    "Corrente (A)": 4,
    "X_L (ohms)": 2,
    "|Z| (ohms)": 2,
    "Fase (°)": 2,
    "V_L teórico (V)": 2,
    "Erro V_L (%)": 2
})

print(df)