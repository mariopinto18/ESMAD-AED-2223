""""
Dado uma conjunto de n números (n indicado pelo utilizador) inteiros
e positivos, determine o segundo maior valor de entre o conjunto de números
lido
"""

primeiroMaior = 0
segundoMaior = 0
n= int(input("Qts numeros dejesa ler? "))
for i in range(n):
    numero = int(input("Número: "))
    if numero > primeiroMaior:
        segundoMaior= primeiroMaior
        primeiroMaior=numero
    elif numero > segundoMaior:
        segundoMaior=numero
print(primeiroMaior, segundoMaior)
