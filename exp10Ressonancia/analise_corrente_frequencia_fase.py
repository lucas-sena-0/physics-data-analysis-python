import numpy as np
import matplotlib.pyplot as plt

R = 100  # Ohms

# Ajuste os vetores abaixo (mesmo número de elementos)
frequencias = np.array([400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700])
tensoes     = np.array([0.6532, 0.742, 1.03, 1.23, 1.62, 2.10, 2.77, 3.33, 3.52, 3.05, 2.57, 2.14, 1.94, 1.70])
deltaT      = np.array([-520e-6, -440e-6, -340e-6, -280e-6, -220e-6, -160e-6, -80e-6, -40e-6, 20e-6, 64e-6, 88e-6 ,96e-6, 112e-6, 116e-6])

# Checagem
if not (len(frequencias) == len(tensoes) == len(deltaT)):
    raise ValueError(f"Tamanhos diferentes: frequencias={len(frequencias)}, tensoes={len(tensoes)}, deltaT={len(deltaT)}")

I = tensoes / R
fase_graus = 360 * deltaT * frequencias

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))
ax1.plot(frequencias, I*1000, 'bo-')
ax1.set_xlabel('Frequência (Hz)')
ax1.set_ylabel('Corrente (mA)')
ax1.set_title('Corrente vs Frequência')
ax1.grid(True, alpha=0.3)

ax2.plot(frequencias, fase_graus, 'ro-')
ax2.axhline(0, color='black', linestyle='--', alpha=0.5)
ax2.set_xlabel('Frequência (Hz)')
ax2.set_ylabel('Fase (°)')
ax2.set_title('Fase vs Frequência (ΔT)')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

print("\nResultados:")
for f, V, dt, i, fase in zip(frequencias, tensoes, deltaT, I, fase_graus):
    print(f"f={f:5.0f} Hz  V={V:.3f} V  ΔT={dt:.6f} s  I={i*1000:.2f} mA  Fase={fase:.2f}°")