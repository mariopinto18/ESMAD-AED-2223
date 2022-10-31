
# Função que recebe um numero e determina se é um numero abundante (True) ou não (False)
def abundante(numero):
    somaDivisores=0
    for i in range (1, numero):  # pecorrer intervaloer de 1 até ao númeor
        resto = numero % i       # se resto ==0, i é um divisor do numero
        if resto ==0:
            somaDivisores+= i
    if somaDivisores>numero:
        return True
    else:
        return False




numero= int(input("Número:"))
if abundante(numero) == True:
    print("o numero {0} é abundante" .format(numero))
else:
     print("o numero {0} NÃO é abundante" .format(numero))
