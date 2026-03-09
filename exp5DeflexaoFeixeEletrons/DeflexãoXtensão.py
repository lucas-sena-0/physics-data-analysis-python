import matplotlib.pyplot as plt
import numpy as np

#DeflexãoXtensão

# Dados
D300 = [0, 0.3, 0.7, 1, 1.35, 1.75, 2.25, 2.65, 3.1, 3.5, 3.8]
D400 = [0, 0.2, 0.55, 0.75, 1.1, 1.4, 1.7, 2.1, 2.4, 2.7, 2.95]
D500 = [0, 0.35, 0.5, 0.8, 1.05, 1.3, 1.6, 1.9, 2.3, 2.6, 2.9]
D600 = [0, 0.2, 0.4, 0.9, 1.0, 1.2, 1.5, 1.8, 2.1, 2.4, 2.6]

# Cálculo da deflexão média
deflexoes_medias = [
    np.mean(D300),
    np.mean(D400),
    np.mean(D500),
    np.mean(D600)
]

# Tensões de aceleração (em volts)
tensoes = [300, 400, 500, 600]

# Plot
plt.figure(figsize=(8,5))
plt.plot(tensoes, deflexoes_medias, 'o-', color='blue', linewidth=2, markersize=8)
plt.xlabel("Tensão de Aceleração (V)", fontsize=12)
plt.ylabel("Deflexão Média do Feixe (cm)", fontsize=12)
plt.title("Deflexão do Feixe em Função da Tensão de Aceleração", fontsize=14)
plt.grid(True)
plt.show()
