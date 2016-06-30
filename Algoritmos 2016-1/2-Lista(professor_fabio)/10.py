
'''
Leia uma data (dia, mês e ano), verifique e escreva se a data é ou não válida.
__ == Dunder
'''
def verifica_data(dia,mes,ano):
    if dia > 0 and dia <= 31:
        if mes > 0 and mes <= 12:
            if ano > 0:
                return ("data valida")
    return("Data ivalida")


def main():
    print("programa verifica data valida")

    dia,mes,ano = int(input("Digite o dia do seu niver\n")),int(input("Digite o mes do seu niver\n")),int(input("Digite o ano do seu niver\n"))

    resultado =   verifica_data(dia,mes,ano)
    print(resultado)
if __name__ == '__main__':
    main()

