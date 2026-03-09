import matplotlib.pyplot as plt
import numpy as np

# Dados
campo = np.array([0.46, 0.64, 0.87, 1.07, 1.26, 1.47, 1.71, 1.89, 2.12, 2.3])  # mT
corrente = np.array([0.31, 0.56, 0.9, 1.19, 1.48, 1.77, 2.12, 2.38, 2.72, 2.97])  # A

# Regressão linear: grau 1
coef = np.polyfit(corrente, campo, 1)
k = coef[0]  # coeficiente angular

print(f"Constante de campo por corrente: {k:.3f} mT/A")

# Dados fornecidos
campo = [0.46, 0.64, 0.87, 1.07, 1.26, 1.47, 1.71, 1.89, 2.12, 2.3]  # em mT
corrente = [0.31, 0.56, 0.9, 1.19, 1.48, 1.77, 2.12, 2.38, 2.72, 2.97]  # em A

# Criando o gráfico
plt.figure(figsize=(8, 5))
plt.plot(corrente, campo, marker='o', linestyle='-', color='blue', label='Campo vs Corrente')
plt.title('Campo Magnético vs Corrente nas Bobinas de Helmholtz')
plt.xlabel('Corrente (A)')
plt.ylabel('Campo Magnético (mT)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()