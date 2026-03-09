import numpy as np
import pandas as pd
#Resistencia interna indutor
Ri = 10

# Dados fornecidos
frequencias = np.array([315, 4617, 10000])  # Hz
R = 100  # ohms
C = 0.47e-6  # farads
V_R_exp = np.array([7.33, 9.9, 9.58])  # V
V_C_exp = np.array([8.32, 0.752, 0.336])  # V

# Cálculo da corrente na malha a partir da queda de tensão no resistor
I = V_R_exp / R  # Corrente (A)

# Reatância capacitiva
X_C = 1 / (2 * np.pi * frequencias * C)

# Impedância total
Z = np.sqrt(R**2 + X_C**2)

# Ângulo de fase (em graus)
phi = -np.arctan(X_C / R) * (180 / np.pi)

# Tensão teórica no resistor e capacitor
V_R_teo = I * R
V_C_teo = I * X_C

# Erros relativos (%)
erro_V_R = (V_R_teo - V_R_exp) / V_R_exp * 100
erro_V_C = (V_C_teo - V_C_exp) / V_C_exp * 100

# Tabela de resultados
df = pd.DataFrame({
    "Frequência (Hz)": frequencias,
    "Corrente (A)": I,
    "X_C (ohms)": X_C,
    "|Z| (ohms)": Z,
    "Fase (°)": phi,
    "V_R teórico (V)": V_R_teo,
    "V_R exp (V)": V_R_exp,
    "Erro V_R (%)": erro_V_R,
    "V_C teórico (V)": V_C_teo,
    "V_C exp (V)": V_C_exp,
    "Erro V_C (%)": erro_V_C
})

# Arredondar para melhor visualização
df = df.round({
    "Corrente (A)": 4,
    "X_C (ohms)": 2,
    "|Z| (ohms)": 2,
    "Fase (°)": 2,
    "V_R teórico (V)": 2,
    "Erro V_R (%)": 2,
    "V_C teórico (V)": 2,
    "Erro V_C (%)": 2
})

print(df)