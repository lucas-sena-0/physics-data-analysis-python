import numpy as np
import pandas as pd

# Dados fornecidos
frequencias = np.array([315, 4617, 10000])  # Hz
R = 100  # ohms
L = 44e-3  # henrys
C = 0.47e-6  # farads
V_L_exp = np.array([1.17, 8.12, 9.7])  # V
V_C_exp = np.array([8.04, 0.5148, 0.1287])  # V

# Cálculo das reatâncias
X_L = 2 * np.pi * frequencias * L
X_C = 1 / (2 * np.pi * frequencias * C)

# Impedância total
Z = np.sqrt(R**2 + (X_L - X_C)**2)

# Ângulo de fase (em graus)
phi = np.arctan((X_L - X_C) / R) * (180 / np.pi)

# Estimativa da corrente na malha (usando soma escalar simplificada das tensões)
V_total = 10  # Vpp da fonte
V_R_est = V_total - V_L_exp - V_C_exp
I = V_R_est / R

# Tensão teórica nos componentes
V_L_teo = I * X_L
V_C_teo = I * X_C

# Erros relativos (%)
erro_V_L = (V_L_teo - V_L_exp) / V_L_exp * 100
erro_V_C = (V_C_teo - V_C_exp) / V_C_exp * 100

# Tabela de resultados
df = pd.DataFrame({
    "Frequência (Hz)": frequencias,
    "X_L (Ω)": X_L,
    "X_C (Ω)": X_C,
    "|Z| (Ω)": Z,
    "Fase (°)": phi,
    "V_R estimado (V)": V_R_est,
    "Corrente (A)": I,
    "V_L teórico (V)": V_L_teo,
    "V_L exp (V)": V_L_exp,
    "Erro V_L (%)": erro_V_L,
    "V_C teórico (V)": V_C_teo,
    "V_C exp (V)": V_C_exp,
    "Erro V_C (%)": erro_V_C
})

# Arredondar para melhor visualização
df = df.round({
    "X_L (Ω)": 2,
    "X_C (Ω)": 2,
    "|Z| (Ω)": 2,
    "Fase (°)": 2,
    "V_R estimado (V)": 2,
    "Corrente (A)": 4,
    "V_L teórico (V)": 2,
    "Erro V_L (%)": 2,
    "V_C teórico (V)": 2,
    "Erro V_C (%)": 2
})

print(df)