import matplotlib.pyplot as plt
import numpy as np
from numpy.polynomial.polynomial import Polynomial

# Dados fornecidos
distancia = np.array([0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5])
campo = np.array([0.83, 0.96, 1.18, 1.4, 1.56, 1.69, 1.78, 1.81, 1.82, 1.84, 1.83, 1.82, 1.78, 1.59, 1.42, 1.2, 1.01, 0.8])

# Ajuste polinomial de grau 4
coef = np.polyfit(distancia, campo, deg=4)
polinomio = np.poly1d(coef)

# Valores ajustados
dist_fit = np.linspace(min(distancia), max(distancia), 200)
campo_fit = polinomio(dist_fit)

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(distancia, campo, 'o', label='Dados experimentais', color='green', linestyle ='-' )
plt.title('Campo Magnético ao Longo do Eixo da Bobina (Corrente = 3A)')
plt.xlabel('Distância ao centro da bobina (polegadas)')
plt.ylabel('Campo Magnético (mT)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()