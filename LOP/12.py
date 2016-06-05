



velocidadePermitida = float(input("Digite a velocidade Permitida na avenida: "))

velocidadeAtual = float(input("Digite a velocidade Atual: "))


velocidadeExcedida = velocidadeAtual - velocidadePermitida

if velocidadePermitida>velocidadeAtual:
	print("Motorista não será multado")
elif(velocidadeExcedida>10):
	print("O Motorista receberá uma multa de R$50")
elif(velocidadeExcedida>11 or velocidadeExcedida<30):
	print("O motorista receberá uma multa de R$100")	
elif(velocidadeExcedida>31):
	print("O motorista receberá uma multa de R$200")
	