


#Leia um número inteiro de metros, calcule e escreva quantos Km e quantos metros ele corresponde.


valor_metros = int(input("Digite o valor em metros: "))

valor_kilometros = valor_metros/1000

valor_final_metros = valor_metros%1000

print("%d km e %d metros"%(valor_kilometros,valor_final_metros))

