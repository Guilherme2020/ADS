from os import system


def main():
	print('\n######VAMOS CADASTRAR OS ALUNOS######\n')
	print("\n#######################################\n")
	menu = ("Digite >>\n1- Para cadastrar novo aluno\n2- Listar Alunos\n3- Limpar Tela \nOu \n0 - para sair\n")

	student = []
	
	verdade = True	
	while verdade:
		
		op = int(input(menu))

		if op == 1:
			print("Vamos cadastrar um novo aluno ")
			student.append(cadastrar_novo_aluno())
		elif op == 2:
			print("Lista dos carinhas cadastrados ate agora ")
			listar_students(student)	
		elif op == 3:
			print("limpando Tela")
			limpa_tela()
		elif op == 0:
			print("Voce saiu do software - Obrigado pela cooperacao ")
			
			break
		else:
			print ('op invalida Tente novamente ou 0 para Sair')		

def limpa_tela():
	
	limpa = system("clear")
	return limpa


def cadastrar_novo_aluno():
	nome = str(input("nome: "))
	idade = str(input("idade: "))
	sexo = str(input("sexo(m(Masculino) ou f(Feminino)): "))
	dicio = {"Nome" : nome,"Idade" : idade,"Sexo" : sexo}
 
	return dicio

def listar_students(student):
	
	for d in student:
		print("Nome %s \nIdade %s \nSexo %s"%(d["Nome"],d["Idade"],d["Sexo"]))
		
	fim =  1 * "##############FIM DO PROCESSAMENTO DE DADOS####"
	print(fim)
if __name__ == '__main__':
	main()	