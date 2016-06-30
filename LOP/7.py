'''
7. Para ler 3 números 
reais do teclado e verificar se o primeiro é maior que a soma dos
outros dois.'''

numberOne = int(input("numberOne- "))
numberTwo = int(input("numberTwo- "))
numberThree = int(input("numberThree- "))


soma = numberTwo+numberThree

if numberOne > soma:
	print("O numeroOne %d é maior que a soma do segundo com o terceiro: "%numberOne)
elif(numberOne == soma):
	print("O numeroOne %d é igual a soma do segundo com o terceiro "%numberOne)
else:
	print("O numeroOne %d é menor que a soma dos segundo com o terceiro: "%numberOne)	