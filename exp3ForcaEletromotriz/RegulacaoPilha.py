import matplotlib.pyplot as plt
from scipy.stats import linregress

# Dados fornecidos
V = [1.27, 1.29, 1.3, 1.3, 1.31, 1.311, 1.312, 1.314, 1.314, 1.315]  # Tensão (V)
I = [0.12, 0.06, 0.04, 0.032, 0.028, 0.024, 0.02, 0.016, 0.014, 0.012]  # Corrente (A)

# Regressão linear (tensão vs corrente)
slope, intercept, r_value, p_value, std_err =  (I, V)
resistencia_interna = -slope  # em ohms

# Gerar pontos da reta ajustada
V_ajustada = [intercept + slope * i for i in I]

# Criar gráfico
plt.figure(figsize=(8, 6))
plt.plot(I, V, 'o', label='Dados experimentais')
plt.plot(I, V_ajustada, 'r-', label=f'Ajuste linear\nRint ≈ {resistencia_interna:.2f} Ω')
plt.title('Curva de Regulação da Pilha')
plt.xlabel('Corrente (A)')
plt.ylabel('Tensão (V)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()