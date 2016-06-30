

'''
Leia a idade de uma pessoa expressa em anos, meses e dias e escreva-a expressa apenas em dias.
'''

anos,meses,dias = int(input("")),int(input("")),int(input(""))

idade_anos = anos*365
idade_meses = meses*30
idade_dias = anos+meses+dias

print(" %d dia(s)"%(dias))

