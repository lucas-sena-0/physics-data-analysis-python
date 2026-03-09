import matplotlib.pyplot as plt

# Dados fornecidos
corrente_A = [0.932, 0.453, 0.246, 0.162, 0.123, 0.099, 0.082, 0.070, 0.060, 0.053, 0.049]
tensao_V = [4.811, 4.951, 4.986, 5.002, 5.011, 5.017, 5.018, 5.023, 5.026, 5.027, 5.03]

# Gerar gráfico
plt.figure(figsize=(8, 6))
plt.plot(corrente_A, tensao_V, marker='o', linestyle='-', color='purple')
plt.title('Tensão vs Corrente – Fonte Comercial')
plt.xlabel('Corrente (A)')
plt.ylabel('Tensão (V)')
plt.grid(True)
plt.tight_layout()
plt.show()