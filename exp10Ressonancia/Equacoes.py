import math

R = 100
L = 44e-3
C = 0.47e-6

w0 = 1/math.sqrt(L*C)
Q = w0/R

print("Q =", Q)
print("w0 =", w0, "rad/s")
print("f0 =", w0/(2*math.pi))

# Constante de tempo (tau) e meia-vida (t_half) para circuito RC
tau = R * C
t_half = tau * math.log(2)

print("tau (RC) =", tau)
print("t_half (Meia-vida) =", t_half)

print("-" * 30)
print("Cálculo do Indutor Desconhecido:")

# Dados do problema
C_novo = 50e-6      # 50 micro Farad
R_novo = 1          # 1 Ohm
f_novo = 10e3       # 10 kHz
fase_graus = 45     # 45 graus

# Conversões
w_novo = 2 * math.pi * f_novo
fase_rad = math.radians(fase_graus)

# Cálculo da Reatância Capacitiva
XC_novo = 1 / (w_novo * C_novo)

# Da fórmula: tan(phi) = (XL - XC) / R
# XL = R * tan(phi) + XC
XL_novo = R_novo * math.tan(fase_rad) + XC_novo

# Como XL = w * L -> L = XL / w
L_desconhecido = XL_novo / w_novo

print(f"Indutância calculada: {L_desconhecido:.6e} H")
print(f"Ou aproximadamente: {L_desconhecido * 1e6:.2f} micro Henry")