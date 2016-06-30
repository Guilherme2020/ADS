
#Importando o modulo inteiro

#importar o arquivo

import calculadora


#importar apenas uma funcao

from calculadora import somar


def main():
    somar(1,2)




if __name__ == '__main__':
    main()


#importar todas as funcoes

from calculadora import *

def main():
    multiplicar(2,3)
    dividir(4,2)
if __name__ == '__main__':
    main()








