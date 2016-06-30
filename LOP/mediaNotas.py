print('''

	CALCULO FINAL



	''')

notaOne = float(input("Digite a sua primeira nota: "))
notaTwo = float(input("Digite a sua segunda nota: "))
notaThree = float(input("Digite a sua terceira nota: "))

mediaFinal = notaOne+notaTwo+notaThree/3

if mediaFinal >= 7:
	print("Aprovado")
elif mediaFinal > 5 or mediaFinal < 7:
	print("Recuperacao")
elif mediaFinal < 5:
	print("Reprovado")




