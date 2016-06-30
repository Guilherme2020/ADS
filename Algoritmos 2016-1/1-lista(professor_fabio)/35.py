


#Leia um número inteiro (4 dígitos), calcule e escreva a soma dos elementos que o compõem. Ex.:
#número = 9534 ; soma = 9+5+3+4 = 21.

numero=int(input("Digite o numero: "))

valor_um=int(numero/1000)

valor_dois=int((numero%1000)/100)

valor_tres=int(((numero%1000)%100)/10)

valor_quatro=int(((numero%1000)%100)%10)

print (valor_um+valor_dois+valor_tres+valor_quatro)
