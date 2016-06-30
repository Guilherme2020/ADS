#
#Leia um valor 
#em minutos, calcule e escreva o equivalente em horas e minutos.
#
	
valor_minutos = int(input(" "))

qtd_minutos_hora = (valor_minutos/60)
qtd_minutos = valor_minutos%60

#horas = (minutos_hora*60) - minutos	

print("%d horas : %d "%(qtd_minutos_hora,qtd_minutos))