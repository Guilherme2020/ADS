

'''3. Calcular a quantidade dinheiro gasta por um fumante. Dados: o número de
 anos que ele
fuma, o no de cigarros fumados por dia e o preço de uma carteira.
'''



numeroAnos = int(input("digite o numero de anos em que a pessoa fuma"))
numeroDecigarros = int(input("Digite o numeros de cigarros por dia"))
valorCigarro= float(input("Quanto custa um cigarro? "))


totalCigarros = numeroDecigarros*numeroAnos*365

dinheiroGasto = totalCigarros*valorCigarro

print(dinheiroGasto)
