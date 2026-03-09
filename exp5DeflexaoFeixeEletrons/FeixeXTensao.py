import matplotlib.pyplot as plt
import numpy as np


# Dados originais
F300 = [0, 0.5, 1.4, 2.1, 2.6, 3.3, 3.8, -0.5, -1.2, -1.8, -2.5, -3.1, -3.9]
V300 = [0.4, 10.1, 20.5, 30.6, 40.6, 50, 60.3, -10.5, -20.6, -30.7, -40.5, -50.5, -60.1]

F400 = [0, 0.35, 0.9, 1.45, 1.8, 2.2, 2.5, -0.4, -0.8, -1.3, -1.7, -2, -2.4]
V400 = [0.4, 10.1, 20.1, 30.3, 39.9, 50.3, 60.3, -10.3, -20.6, -30.6, -40.2, -50, -60.1]

F500 = [0, 0.35, 0.85, 1.3, 1.6, 1.9, 2.2, -0.35, -0.7, -1.1, -1.3, -1.7, -2]
V500 = [0.3, 10.5, 20.3, 30.5, 40.2, 50.1, 60.4, -10.6, -20.6, -30.8, -40.1, -50.1, -60.2]

F600 = [0, 0.3, 0.75, 1.1, 1.4, 1.65, 1.9, -0.25, -0.55, -0.9, -1.1, -1.35, -1.65]
V600 = [1, 10.9, 20.9, 31.2, 40.1, 50.3, 60.5, -10.1, -20.3, -30.4, -39.8, -50, -60.4]

# Parâmetros de erro
erro_V = 0.05
erro_F = 0.05

# Função para calcular e plotar regressão com barras de erro
def plot_regressao_com_erro(V, F, cor, rotulo):
    if len(V) == 0 or len(F) == 0:
        return
    V_np = np.array(V)
    F_np = np.array(F)
    a, b = np.polyfit(V_np, F_np, 1)
    V_fit = np.linspace(min(V_np), max(V_np), 100)
    F_fit = a * V_fit + b
    plt.errorbar(V, F, xerr=erro_V, yerr=erro_F, fmt='o', color=cor, label=f'{rotulo} pontos ±0.05')
    plt.plot(V_fit, F_fit, '-', color=cor, label=f'{rotulo} ajuste')

# Plot
plt.figure(figsize=(10, 7))
plot_regressao_com_erro(V300, F300, 'green', 'F300')
plot_regressao_com_erro(V400, F400, 'blue', 'F400')
plot_regressao_com_erro(V500, F500, 'red', 'F500')
plot_regressao_com_erro(V600, F600, 'purple', 'F600')  # Será ignorado se estiver vazio

plt.xlabel('Tensão (V)')
plt.ylabel('Deflexão (Cm)')
plt.title('Gráfico da Deflexão por variação da tensão')
plt.legend()
plt.grid(True)
plt.show()
