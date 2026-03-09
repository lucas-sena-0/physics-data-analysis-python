import matplotlib.pyplot as plt

# Dados fornecidos
Dist = [0, 1.5, 3, 4.5, 6, 7.5, 9, 10.5, 12, 13.5, 15, 16.5, 18, 19.5, 21]
campo = [0.96, 1.40, 1.79, 1.94, 2.01, 2.05, 2.06, 2.07, 2.05, 2.09, 2.02, 1.99, 1.84, 1.47, 1.09]

# Criando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(Dist, campo, marker='o', linestyle='-', color='green', label='Campo Magnético')
plt.title('Campo Magnético ao Longo da Distância')
plt.xlabel('Distância (cm)')
plt.ylabel('Campo Magnético (mT)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()