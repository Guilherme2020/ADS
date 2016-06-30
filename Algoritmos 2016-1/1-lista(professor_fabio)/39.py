
'''

Leia três números inteiros e positivos (A, B, C) e calcule a seguinte expressão:

D = R+S/2

R = (A+B)²
S = (B+C)²


'''

from math import sqrt, pow

valor_a = int(input("Digite o valor de a:  "))

valor_b = int(input("Digite o valor de b:  "))

valor_c = int(input("Digite o valor d c:   "))

valor_r = valor_a+valor_b

valor_s = valor_b+valor_c

R = pow(valor_r,2)

S = pow(valor_s,2)

D = (R+S)/2

print("O valor da expressão é: %d"%(D))
