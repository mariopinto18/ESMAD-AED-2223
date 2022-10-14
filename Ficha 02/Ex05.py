## ler 3 numeros e imprimir por ordem crescente

num1 = int(input("Indique o primeiro numero:"))
num2 = int(input("Indique o segundo numero:"))
num3 = int(input("Indique o terceiro numero:"))

if num1 < num2:     
    if num2 < num3:         # num1, num2, num3
        print(num1, num2, num3)
    elif num1 < num3:       # num1, num3, num2
        print(num1, num3, num2)
    else:                  # num3 é o + pequeno, porque a condição anterior falhou
        print(num3, num1, num2)
elif num2 < num3:      # Atenção que nesta fase num2 <= num1
    if num1 < num3:
        print(num2, num1, num3)
    else:
        print(num2, num3, num1)
else:
    print(num3, num2, num1)

