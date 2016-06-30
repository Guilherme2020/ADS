


#Leia um número inteiro de meses, calcule e escreva quantos anos e quantos meses ele corresponde.
#

valor_meses = int(input("Digite o valor em meses: \n"))

valor_anos = valor_meses/12
valor_final_meses = valor_meses%12

print("%d mese(s) equivalem a %d ano(s) e %d mese(s)"%(valor_meses,valor_anos,valor_final_meses))

