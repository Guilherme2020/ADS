#Leia uma temperatura em °F, calcule e escreva a equivalente em °C. (t°C = (5 * t°F - 160) / 9).


temperatura_farenhit = float(input("Digite a temperatura em °F:  "))

temperatura_celsius = ((5*temperatura_farenhit)-160)/9

print("%.2f°F equivalem a %.2f°C "%(temperatura_farenhit,temperatura_celsius))



