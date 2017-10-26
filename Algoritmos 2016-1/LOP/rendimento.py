''' 
	Juliana,	 irá	 viajar	 no	 final	 de	 semana		
ela	 Precisa	 saber	 quantos	
litros	de	combustível	será	necessário	para	ir	e	voltar	a	
partir	 Teresina,	 em	 seu	 Toyota	 Corolla,	 que	 faz	 em
média	 14	 Km/l,	 quando	 abastecido	 com	 Gasolina,	 ou	
10	Km/l,	quando	Álcool.

'''


cityOne = input("Qual o nome da Primeira cidade? ")
ciryTwo = input("QUal o nome da Segunda Cidade? ")

distancia=  float(input("QUal a distanca entra as cidades ?"))

rendimentoGasolina = float(input("Qual o rendiment com gasolina? "))
rendimentoAlcool = float(input("Qual o seu rendimento com Alcool? "))


totalGasolina = distancia/rendimentoGasolina
totalGasolina = totalGasolina*3.5

totalAlcool = distancia/rendimentoAlcool
totalAlcool = totalAlcool*2.9


tipoCombustivel = int(input("digite 1 para gasolina e 2 para alcool: "))

if tipoCombustivel == 1:

	
	print("Voce deve colocar $$ %.2f Em gasolina "%totalGasolina)
	print("Mas se tivesse escolhido alcool seria $$ %.2f"%totalAlcool)

elif tipoCombustivel == 2:
	print("Voce deve colocar $$ %.2f em Alcool "%totalAlcool)
	print("Mas se tivesse escolhido Gasolina seria $$ %d"%totalGasolina)



