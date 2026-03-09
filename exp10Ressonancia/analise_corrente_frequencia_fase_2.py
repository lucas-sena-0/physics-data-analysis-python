import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do circuito
R = 1000          # Ohms
frequencias = np.array([400, 500, 600, 700, 800, 900, 1000,
                        1100, 1200, 1300, 1400, 1500, 1600, 1700])

# --- Simulação experimental aproximada ---
# Valores baseados em comportamento esperado, com pequenas variações
# Corrente é menor que no caso de 100Ω, pico próximo à ressonância
tensoes_base = np.array([0.35, 0.42, 0.55, 0.70, 0.95, 1.25, 1.60,
                         1.95, 2.05, 1.80, 1.55, 1.30, 1.15, 1.00])

# Adiciona pequenas flutuações aleatórias (±5%)
rng = np.random.default_rng(42)  # semente fixa para reprodutibilidade
tensoes = tensoes_base * (1 + 0.05*rng.standard_normal(len(tensoes_base)))

# ΔT simulado: negativo antes da ressonância, cruza zero em ~1150 Hz
deltaT_base = np.array([-280e-6, -240e-6, -200e-6, -160e-6, -120e-6, -80e-6,
                        -40e-6, -10e-6, 20e-6, 50e-6, 70e-6, 85e-6, 95e-6, 100e-6])
deltaT = deltaT_base * (1 + 0.1*rng.standard_normal(len(deltaT_base)))

# Corrente
I = tensoes / R

# Fase em graus aproximada
fase_graus = 360 * deltaT * frequencias

# --- Gráficos ---
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 8))

ax1.plot(frequencias, I*1000, 'bo-')
ax1.set_xlabel('Frequência (Hz)')
ax1.set_ylabel('Corrente (mA)')
ax1.set_title('Corrente vs Frequência (R=1000Ω)')
ax1.grid(True, alpha=0.3)

ax2.plot(frequencias, fase_graus, 'ro-')
ax2.axhline(0, color='black', linestyle='--', alpha=0.5)
ax2.set_xlabel('Frequência (Hz)')
ax2.set_ylabel('Fase (°)')
ax2.set_title('Fase vs Frequência (R=1000Ω)')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# --- Impressão dos resultados ---
print("\nResultados simulados (aproximados):")
for f, V, dt, i, fase in zip(frequencias, tensoes, deltaT, I, fase_graus):
    print(f"f={f:5.0f} Hz  V={V:.3f} V  ΔT={dt:.6f} s  I={i*1000:.2f} mA  Fase={fase:.2f}°")
