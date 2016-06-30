#10
'''. Ler 2 números 
inteiros do teclado (A e B), 
verificar e imprimir qual deles é o maior, ou a
mensagem “A=B” caso sejam iguais.'''


cont = True
while cont:
		
	try:
			
		a = int(input("A:Insira o valor de A ou 0 para sair:>> "))
		if(a == 0 ):
			break
		b = int(input("B:Insira o valor de B:>> "))
		if(a>b):
			print("A é maior que B")
			break
		elif(b>a):
			print("B é maior que A: ")
			break
		elif(a==b):
			print("A e B são iguais: ")
			break
		
	except ValueError as e:
		print("Ouve um problema Tente novamente(vc inseriu textos ao inves de numeros:>",e)




