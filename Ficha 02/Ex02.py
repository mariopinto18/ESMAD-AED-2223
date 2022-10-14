# classificar um triângulo lendo as medidas dos 3 lados

lado1 = float(input("Medida do lado 1 (cm): "))
lado2 = float(input("Medida do lado 2 (cm): "))
lado3 = float(input("Medida do lado 3 (cm): "))

if lado1 <=0 or lado2 <=0 or lado3 <= 0:
    print("Não é um triangulo, pf insira medidas superiores a 0")
elif lado1 == lado2 and lado1 == lado3:
    print("o triangulo é equilátero")
elif lado1 != lado2 and lado1!= lado3 and lado2 != lado3:
        print("o triangulo é escaleno")
else:
    print("o triangulo é isósceles")


    