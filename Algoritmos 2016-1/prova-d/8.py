#questao triangulo



a = float(input(""))

b = float(input(""))

c = float(input(""))

if ((a > (b-c)) and (a < b+c) and  (b > (a-c)) and (b < a+c) and  (c>(a-b)) and (c<a+b)):

    perimetro = a+b+c
    print("Perimetro %.f"%(perimetro))
else:
    area_trapezio = ((a+b)/2)*c
    print("Area = %.2f"%(area_trapezio))

