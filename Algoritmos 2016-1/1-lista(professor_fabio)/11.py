'''
Leia um número inteiro (3 dígitos) 
e escreva o inverso do número. (Ex.: número = 532 ; inverso = 235) 
'''


multi = 0
num_tres_digitos = int(input("  "))

n1 = int(num_tres_digitos/100)
multi = num_tres_digitos - (n1*100)
n2 = int(multi/10)
n3 = num_tres_digitos-((n1*100)+(n2*10))
invertido = (n3*100)+(n2*10)+(n1)
print("O numero invertido e %d\n"%(invertido))


#modo facil do python
'''num = input("")
print (num[::-1])'''