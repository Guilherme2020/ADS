#Leia um número inteiro (3 dígitos),
# calcule e escreva a soma de seus elementos (C + D + U).


valor = int(input("Digite um valor inteiro  de 3 digitos "))

c = valor/100
d = (valor%100)/10
u = (valor%10)

soma_elementos = c+d+u
print("A soma dos tres digitos do valor %d eh %d "%(valor,soma_elementos))