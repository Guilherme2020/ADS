

# Ano bissexto


ano = int(input(""))

if ano%400 == 0 and ano%4==0:
	print("eh bissexto")
elif ano%100 ==0:
	print("nao eh bissexto")	