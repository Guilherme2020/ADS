
cont = True
while(cont):

	nome = str(input("Entre com seu nome ou 0 para sair "))
	if int(nome) == 0:
		break
	elif nome != 'Guilherme':
		print("Nome incorreto,Tente novamente")
	else:
		print("Nome correto")
		break		

		