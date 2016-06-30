#Leia um número inteiro de segundos, calcule e escreva quantas horas, quantos minutos e quantos
#segundos ele corresponde.

valor_segundos = int(input("Digite o valor em segundos: "))

valor_horas =   valor_segundos/3600

valor_segundos = valor_segundos%3600

valor_minutos = valor_segundos/60

valor_segundos = valor_segundos%60

print("%d:%d:%d"%(valor_horas,valor_minutos,valor_segundos))