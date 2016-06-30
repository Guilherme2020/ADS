#Leia uma velocidade em km/h, 
#calcule e escreva esta velocidade em m/s. (Vm/s = Vkm/h / 3.6)


velocidade_kmh = float(input("Insira a velocidade em km/h"))

velocidade_metros_segundo  = velocidade_kmh/3.6

print(" %.2fKm/h equivale a %.2f m/s "%(velocidade_kmh,velocidade_metros_segundo))

