
cont = 0
a = int(input("Digite o primeiro numero"))
b = int(input("Digite o segundo numero"))
c = int(input("Digite o terceiro numero"))



if a == b:
	cont +=1
if a == c:
	cont+=1
if c == b:
	cont+=1

print("A quantidade de numeros iguais eh %d"%(cont))		