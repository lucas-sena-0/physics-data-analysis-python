import numpy as np

# Dados
V = 220.9  # tensão de aceleração
r = np.array([5, 4, 3, 2])  # raios em cm
I = np.array([1.418, 1.753, 2.361, 3.656])  # correntes em A
constIB = 0.689  # constante B por I (mT/A)
razReal = 1.7588e+11

# Cálculo do campo magnético B
B = I * constIB  # em mT
B = B / 1000  # convertendo para tesla

# Convertendo raio para metros
r = r / 100  # cm → m

# Fórmula: e/m = 2V / (B² * r²)
valorCM = (2 * V) / (B**2 * r**2)

# Exibindo os resultados
print("Razão e/m para cada caso (C/kg):")
print(valorCM)
print(np.mean(valorCM))
print ("Erro = ",1-np.mean(valorCM)/razReal)