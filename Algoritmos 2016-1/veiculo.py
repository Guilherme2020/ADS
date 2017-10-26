


from os import system

def main():


	menu = "1-Cadastrar novo carro\n2-Listar Carros"\
	"\n3-Excluir Carros\n4-Editar\n5-Limpar A tela"\
	"\n0-sair\n"
	#print(menu)
	bd_carro = inicializar()
	
	
	while True:	
		op = int(input(menu))

		if op == 1:
			carro = cadastrar_novo_carro()
			bd_carro.append(carro)
		elif op == 2:
			listar_carros(bd_carro)
		elif op == 3:
			deletar_carro(bd_carro)
		elif op == 4: 
			pass
		elif op == 5:
			limpar_tela()
		elif op == 0:
			finalizar(bd_carro)
			print("Saiu")	
			break
		else:
			print("Opco invalida")	
	print("Final")		

def limpar_tela():
	limpa = system("clear")
	return limpa

def inicializar():
	arquivo_veiculos = open("arquivo_veiculos.txt","r")
	linhas = arquivo_veiculos.readlines()
	veiculos = []

	for linha in linhas:
		veiculos.append(eval(linha))
	
	arquivo_veiculos.close()
	
	return veiculos	


def finalizar(lista):
	arquivo = open("arquivo_veiculos.txt","w")

	for c in lista:
		arquivo.write(str(c) + '\n')

	arquivo.close()		



def cadastrar_novo_carro():
	id_veiculo = int(input("Id: "))
	nome = str(input("Nome: "))
	valor = float(input("Valor: "))
	montadora = str(input("Montadora: "))
	data_frabicacao = int(input("Data: "))

	dicio = {"Id":id_veiculo,"Nome":nome,"Valor":valor,"Montadora":montadora,"Data":data_frabicacao}

	return dicio

def ultimo_id():
	inicio =  inicializar()

def deletar_carro(bd_carro):
	listar_carros(bd_carro)
	posicao = int(input('Qual indice? '))
	#del bd_alunos[posicao]
	removido = bd_carro.pop(posicao)
	print ('Carro: ', removido['Nome'], ' removido.')



def editar_carro(bd_carro):
'''	listar_carros(bd_carro)
	posicao = int(input(""))

	atualizado = bd_carro (posicao)
'''
	'''editar = input("")
			
				for i in range(bd_carro):
					if editar == bd_carro[i].get(no)
			'''
def listar_carros(bd_carro):
	#print ('Carros Cadastrados (%d)' % len(bd_carro))
	for c in bd_carro:
		#print(i,bd_carro[]["Nome"],bd_carro[]["Valor"],bd_carro[]["Montadora"],bd_carro["Data"])
		print("Id-> %d \nNome-> %s \nValor->%.2f \nMontadora->%s \nData %d "%(c["Id"],c["Nome"],c["Valor"],c["Montadora"],c["Data"]))
	
if __name__ == '__main__':
		main()	






