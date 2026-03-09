import matplotlib.pyplot as plt

# Tensão constante (em volts)
V = 0.000556  # 0,556 mV

# Correntes medidas (em mA)
correntes_mA = [51.94, 26.41, 17.68, 13.44, 10.72, 8.96, 7.57, 6.64, 5.90]

# Converter para ampères
correntes_A = [i / 1000 for i in correntes_mA]

# Calcular resistência equivalente para cada ponto: R = V / I
resistencias_ohm = [V / i for i in correntes_A]

# Gerar gráfico
plt.figure(figsize=(8, 6))
plt.plot(correntes_A, resistencias_ohm, marker='o', linestyle='-', color='green')
plt.title('Resistência Equivalente vs Corrente (Fonte Estabilizada)')
plt.xlabel('Corrente (A)')
plt.ylabel('Resistência Equivalente (Ω)')
plt.grid(True)
plt.tight_layout()
plt.show()