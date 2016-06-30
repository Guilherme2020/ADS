'''
Leia um número inteiro de minutos, calcule e escreva quantos dias, quantas horas e quantos minutos ele
corresponde.

'''

valor_minutos = int(input("Digite o valor em minutos: "))

valor_dias = valor_minutos/1440
valor_horas = (valor_minutos%1440)/60
valor_final_minutos = (valor_minutos%1440)%60

