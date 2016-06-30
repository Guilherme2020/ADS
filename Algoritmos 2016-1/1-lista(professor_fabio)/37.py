

idade_dias = int(input("Digite a idade da pessoa em dias: "))

idade_anos = idade_dias/365

idade_meses = (idade_dias%365)/30

idade_dias = (idade_dias%365)%30

print("%d ano(s) %d mese(s) %d dia(s) "%(idade_anos,idade_anos,idade_dias))

