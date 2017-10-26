


cidade_one = input("Qual a primeira cidade: ")
cidade_two = input("Qual a segunda cidade: ")
distancia_cidade = float(input("Digite a distancia entre as cidades em km/l: "))

rendimento_gasolina = float(input("Qual o rendimento com gasolina? "))

rendimento_alcool = float(input("Qual o rendimento com alcool? "))

total_gas = ((distancia_cidade*2)/rendimento_gasolina)*3.5

total_alcool = ((distancia_cidade*2)/rendimento_alcool)*2.9

#total_alcool = total_alcool*2.9
#or valor((d*2)/r)*valor_litro > gas ou alcool

pergunta = int(input("Qual voce prefere 1(gasolina) 2- Alcool "))

if pergunta == 1:
	print("A primeira cidade er",cidade_one)
	print("A segunda cidade é ",cidade_two)
	print("para ida e volta voce deve colocar R$ %.2f"%(total_gas))
	print("Porem se tivesse escolhido alcool seria R$ %.2f"%(total_alcool))
elif pergunta == 2:
	print("A primeira cidade er",cidade_one)
	print("A segunda cidade é ",cidade_two)
	print("para ida e volta  voce  deve colocar R$ %.2f"%(total_alcool))
	print("Poerem se tivesse escolhido gasolina o valor seria R$ %.2f"%(total_gas))


	 





