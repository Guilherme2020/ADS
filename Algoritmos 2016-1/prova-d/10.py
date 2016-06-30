'''
com  laço for

def tabuada(valor, multiplicado_por):
    for i in range(10 - (multiplicado_por - 1)):
        print('{} x {} = {}'.format(valor, (multiplicado_por + i), (valor * (multiplicado_por + i))))
tabuada(6,3)

'''

#tabuada(6,3)
#da forma certa recursivamente

def tabuada(valor,contador=1):
    if contador > 10:
        print("fim")
    else:
        print("%d x %d = %d" %(valor,contador, valor*contador))
        tabuada(valor,contador+1)

def main():
    numero_um = int(input("tabuada de: "))
    numero_dois = int(input("comecando de: "))
    tabuada(numero_um,numero_dois)

if __name__ == '__main__':
    main()
