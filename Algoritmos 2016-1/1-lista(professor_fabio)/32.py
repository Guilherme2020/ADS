#Leia um número inteiro (3 dígitos), calcule e escreva a diferença entre o número e seu inverso.




multi = 0
num_tres_digitos = int(input("  "))

n1 = int(num_tres_digitos/100)
multi = num_tres_digitos - (n1*100)
n2 = int(multi/10)
n3 = num_tres_digitos-((n1*100)+(n2*10))
invertido = (n3*100)+(n2*10)+(n1)
calculo = num_tres_digitos-invertido
print("O numero invertido e %d\n"%(invertido))
print("A diferença do numero invertido com o numero digitado eh %d"%calculo)