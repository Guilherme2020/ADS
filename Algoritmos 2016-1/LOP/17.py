
from math import sqrt



valueA,valueB,valueC = [int(i) for i in raw_input("").split(" ")]  

delta = valueB*valueB - 4*valueA*valueC
if((valueA!=0) and (delta > 0 )):
    delta = sqrt (delta)
    x1 = (-valueB) + (delta)
    x2 = (-valueB) - (delta)

    x1 = x1 / 2*valueA
    print("R1 = %.5f"%x1)
    x2 = x2 / 2*valueA
    print("R2 = %.5f"%x2)
else:
    print("impossivel calcular\n")


