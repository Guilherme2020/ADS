#Leia o valor do raio de uma esfera, calcule e escreva seu volume. (v = (4 * p * r³)/3) (pi = 3,14)

from math import sqrt, pow

raio_esfera = float(input("Digite o valor do raio da esfera: "))

volume_esfera = (4*3.14*sqrt(raio_esfera,3))/3

print("O volume da esfera eh %.2f"%(volume_esfera))

