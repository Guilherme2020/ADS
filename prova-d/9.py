#Escreva um programa que receba um número inteiro e
#que recursivamente escreva os seus 10 primeiros múltiplos.



def multiplo(numero,contador=1):
	if contador == 10:
		print("numero x contador =  %d " %(numero*contador))
	else:
		print("numero x contador = %d"%(numero*contador))
		multiplo(numero,contador+1)

def main():
	numero = int(input("Digite o numero para ver os 10 primeiros multiplos dele: "))
	multiplo(numero)

if __name__ == "__main__":
	main()