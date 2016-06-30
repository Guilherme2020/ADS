

#Leia um número inteiro de horas, calcule e escreva quantas semanas, quantos dias e quantas horas ele
#corresponde.

valor_horas = int(input("Digite o valor em horas:  "))

valor_semanas = valor_horas/168
valor_dias = (valor_horas%168)/24
valor_horas = (valor_horas%168)%24

print("%d semana(s) %d dia(s) %d hora(s)"%(valor_semanas,valor_dias,valor_horas))