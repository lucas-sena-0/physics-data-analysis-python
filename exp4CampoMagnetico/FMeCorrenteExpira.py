import matplotlib.pyplot as plt
import numpy as np

# Aceleração da gravidade
g = 9.81  # m/s²

# Dados originais
I1 = [0, 0.488, 0.981, 1.511, 2.005, 2.522, 3.001, 3.493, 3.964, 4.476, 4.851]
P1 = [29.52, 29.73, 29.81, 29.92, 29.94, 29.97, 30.02, 30.07, 30.08, 30.09, 30.1]

I2 = [0, 0.48, 0.989, 1.5, 1.991, 2.482, 3.072, 3.482, 3.991, 4.491, 4.843]
P2 = [30.1, 30.21, 30.33, 30.61, 30.74, 30.91, 31.11, 31.22, 31.46, 31.55, 31.783]

I3 = [0, 0.519, 0.999, 1.505, 2.008, 2.490, 2.993, 3.476, 3.987, 4.53, 4.843]
P3 = [35.12, 35.52, 35.91, 36.31, 36.71, 37.01, 37.35, 37.76, 38.06, 38.41, 38.71]

I4 = [0, 0.492, 1.015, 1.504, 1.997, 2.496, 2.998, 3.506, 4.005, 4.867]
P4 = [32.32, 33.17, 33.91, 34.61, 35.35, 36.14, 36.91, 37.71, 38.51, 39.87]

# Função para calcular força
def calcula_forca(pesos):
    peso_inicial = pesos[0]
    massa = [(p - peso_inicial) / 1000 for p in pesos]  # convertendo g para kg
    return [m * g for m in massa]

# Vetores de força
F1 = calcula_forca(P1)
F2 = calcula_forca(P2)
F3 = calcula_forca(P3)
F4 = calcula_forca(P4)

# Regressões lineares
coef1 = np.polyfit(I1, F1, 1)
regressao1 = np.poly1d(coef1)

coef2 = np.polyfit(I2, F2, 1)
regressao2 = np.poly1d(coef2)

coef3 = np.polyfit(I3, F3, 1)
regressao3 = np.poly1d(coef3)

coef4 = np.polyfit(I4, F4, 1)
regressao4 = np.poly1d(coef4)

# Geração dos valores ajustados
I1_fit = np.linspace(min(I1), max(I1), 100)
F1_fit = regressao1(I1_fit)

I2_fit = np.linspace(min(I2), max(I2), 100)
F2_fit = regressao2(I2_fit)

I3_fit = np.linspace(min(I3), max(I3), 100)
F3_fit = regressao3(I3_fit)

I4_fit = np.linspace(min(I4), max(I4), 100)
F4_fit = regressao4(I4_fit)

# Plot
plt.figure(figsize=(10, 6))

plt.plot(I1, F1, 'o', color='green', label='Expira 12.5')
plt.plot(I1_fit, F1_fit, '-', color='green', label=f'Regressão L1: y = {coef1[0]:.3f}x + {coef1[1]:.3f}')

plt.plot(I2, F2, 'o', color='blue', label='Expira 25')
plt.plot(I2_fit, F2_fit, '-', color='blue', label=f'Regressão L2: y = {coef2[0]:.3f}x + {coef2[1]:.3f}')

plt.plot(I3, F3, 'o', color='orange', label='Expira 50')
plt.plot(I3_fit, F3_fit, '-', color='orange', label=f'Regressão L3: y = {coef3[0]:.3f}x + {coef3[1]:.3f}')

plt.plot(I4, F4, 'o', color='red', label='Expira 100')
plt.plot(I4_fit, F4_fit, '-', color='red', label=f'Regressão L4: y = {coef4[0]:.3f}x + {coef4[1]:.3f}')

plt.title('Corrente vs Força - Expira 12.5/25/50/100')
plt.xlabel('Corrente (A)')
plt.ylabel('Força (N)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()