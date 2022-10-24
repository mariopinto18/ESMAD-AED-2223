# Ler n números e indicar o maior e a média
import math

maior = -math.inf   # inicializar a variavel maior com o menor numero 
soma =0
qt = int(input("quantos números deseja ler?"))
for i in range(qt):
    numero = int(input("Indique um número: "))
    soma+=numero
    if numero > maior:
        maior = numero

print("A média é {:.2f}" .format(soma/qt))
print("o maior valor é {0}" .format(maior))

input()