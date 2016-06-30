#error
def multiplo(numero):
    if numero <0:
        return 1
    else:
        if numero % 2== 0:
            print(numero)
            print(numero+1)
def main():
    multiplo_numero = int(input("numero: "))
    resultado = multiplo(multiplo_numero)
    print (resultado)
if __name__ == '__main__':
    main()