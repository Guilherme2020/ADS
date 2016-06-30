#Leia a razão de uma PA 
#(Progressão Aritmética) e o seu primeiro e último termos e
#informe a soma dos elementos dessa PA.
'''
	# Uma PA tem a formula
	# an = a1+(n-1)*r
	#onde an = Termo geral
	#a1 primeiro termo da sequencia
	n = Número de termos da P.A. ou posição 
	do termo numérico na P.A
	r = Razão
'''


r = float(input("insira a razao da PA: "))
a1 = float(input("insira o primeiro termo da PA: "))
an = float(input("insira o ultimo termo da PA: "))

#processamento errado
#soma = ((a1+an)*((an-a1(+r)/r)))/2

soma = ((a1+an)*((an-a1+r)/r))/2;


if((a1 == an)and(r!=0) or (a1 != an) and (r == 0)):
	print("\nIsto é impossivel na matematica\n")
elif(a1==an and r==0):
	n = float(input("Entre com o numero de termos: "))
	print("\nSoma da PA: %f\n"%(n*a1))
else:
	print("\nSoma dos termos da pa é igual a %.2f"%(soma))




