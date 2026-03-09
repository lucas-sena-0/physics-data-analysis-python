import matplotlib.pyplot as plt

# Tensão constante da fonte (em volts)
V = 0.000556  # 0,556 mV

# Correntes medidas (em mA)
correntes_mA = [51.94, 26.41, 17.68, 13.44, 10.72, 8.96, 7.57, 6.64, 5.90]

# Converter para ampères
correntes_A = [i / 1000 for i in correntes_mA]

# Calcular V/I para cada ponto
valores_V_por_I = [V  for i in correntes_A]

# Gerar gráfico
plt.figure(figsize=(8, 6))
plt.plot(correntes_A, valores_V_por_I, marker='o', linestyle='-', color='darkorange')
plt.title('Gráfico de Tensão vs Corrente – Fonte Estabilizada')
plt.xlabel('Corrente (A)')
plt.ylabel('Tensão (V)')
plt.grid(True)
plt.tight_layout()
plt.show()