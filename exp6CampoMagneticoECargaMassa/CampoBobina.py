import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Dados fornecidos
Dist = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
Campo = [0.18, 0.24, 0.33, 0.43, 0.56, 0.71, 0.87, 1.05, 1.22, 1.35, 1.41,
         1.3, 1.19, 1.03, 0.85, 0.66, 0.51, 0.40, 0.29, 0.2, 0.13]

# Converter para numpy arrays
x = np.array(Dist)
y = np.array(Campo)

# Definir função de ajuste (gaussiana)
def gaussiana(x, a, x0, sigma):
    return a * np.exp(-(x - x0)**2 / (2 * sigma**2))

# Ajuste dos dados
popt, pcov = curve_fit(gaussiana, x, y, p0=[1.5, 0, 5])
a_fit, x0_fit, sigma_fit = popt
erros = np.sqrt(np.diag(pcov))
print(erros)
relativo = erros / popt
print(relativo)

# Gerar curva ajustada
x_fit = np.linspace(min(x), max(x), 1000)
y_fit = gaussiana(x_fit, a_fit, x0_fit, sigma_fit)

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'o', label='Dados experimentais', color='blue')
plt.plot(x_fit, y_fit, '-', label='Ajuste Gaussiano', color='red')
plt.title('Intensidade do Campo Magnético vs Distância da Bobina')
plt.xlabel('Distância da Bobina (polegadas)')
plt.ylabel('Intensidade do Campo Magnético (mT)')
plt.axvline(0, color='gray', linestyle='--')
plt.grid(True)
plt.legend()
plt.show()