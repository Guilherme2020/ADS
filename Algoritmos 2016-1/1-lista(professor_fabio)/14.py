#Leia 3 notas de um aluno e o peso de cada nota, calcule e escreva a média ponderada.


nota_one = float(input("Digite a primeira nota: "))

nota_two = float(input("Digite a segunda nota: "))

nota_three = float(input("Digite a terceira nota: "))

peso_one = float(input("Digite o valor do  peso da nota um: "))

peso_two = float(input("Digite o valor do peso da nota dois: "))

peso_three = float(input("Digite o valor do peso da nota três: "))

media_ponderada = ((nota_one*peso_one)+(nota_two*peso_two)+(nota_three*peso_three))/(peso_one+peso_two+peso_three)

print("A media ponderada do aluno equivale a %.2f "%(media_ponderada))


