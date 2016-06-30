#Leia o valor do lado de um quadrado, calcule e escreva sua area. (area = lado²)

from math import sqrt, pow

lado_quadrado = float(input("Digite o valor do lado do quadrado: "))



area_quadrado = pow(lado_quadrado,2)

print("A area do quadrado eh igual a %.2f"%(area_quadrado))