

'''
   Leia uma temperatura em °C, calcule e escreva a equivalente em °F. (t°F = (9 * t°C + 160) / 5)


'''

temperatura_celsius = float(input("Digite a temperatura em °C "))

temperatura_fahenhit = ((9*temperatura_celsius)+160)/5

print(" %.2f°C equivale ah %.2f°F "%(temperatura_celsius,temperatura_fahenhit))