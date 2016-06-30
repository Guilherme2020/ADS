


def calcula_salario(qtd_aula,valor_hora):

    salario = qtd_aula * valor_hora

    return salario

def compara_salarios(salario_prof_one,salario_prof_two):
    '''pass

    salario_prof_one = calcula_salario(qtd_horas_prof_one*valor_hora_prof_one)

    salario_prof_two = calcula_salario(qtd_horas_prof_two*valor_hora_prof_two)


    if salario_prof_one > salario_prof_two:
        print("Professor 1 ganha mais")
    elif salario_prof_two > salario_prof_one:
        print("Professor 2 ganha mais")
    else:
        print("Os salarios dos dois sao iguais")

    '''
def main():
    print("Calcula salario $R$")

    qtd_horas_prof_one,valor_hora_prof_one  = int(input("Quantidade de horas prof1: ")),float(input("Valor da hora prof1: "))
    qtd_horas_prof_two,valor_hora_prof_two = int(input("Quantidade de horass prof2: ")),float(input("Valor da Horas prof2: "))

    salario_prof_one = calcula_salario(qtd_horas_prof_one*valor_hora_prof_one)
    salario_prof_two = calcula_salario(qtd_horas_prof_two*valor_hora_prof_two)


    #Compara salarios
    print("Professor 1 ganha"%(salario_prof_one))
    print("Professor 2 ganha"%(salario_prof_two))

    if salario_prof_one > salario_prof_two:
        print("Professor 1 ganha mais")
    elif salario_prof_two > salario_prof_one:
        print("Professor 2 ganha mais")
    else:
        print("Os salarios dos dois sao iguais")


if __name__ == '__main__':
    main()