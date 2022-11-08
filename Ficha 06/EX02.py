import random

def generateNumbers(lim_inf, lim_sup, qt):
    """
    generates qt random values ​​between lim_inf and lim_sup
    returns a list of the generated random values
    """
    chave = []
    i=0
    while i <qt:
        numero = random.randint(lim_inf,lim_sup)    # gera nº aleatorio
        if numero not in chave:                     # se nº gerado NAO existe na lista
            chave.append(numero)                    # acrescenta à lista
            i+=1
    return chave


# Inicio da execução do programa
op = "S"
while op.upper() == "S":
    chave = []
    estrelas = []
    chave = generateNumbers(1,50,5)     # gerar 5 numeros entre 1 e 50
    estrelas = generateNumbers(1,12,2)   # gerar 2 estrelas entre 1 e 12

    print("\n Chave do Euromilhões: ", chave, "\t Estrelas: ", estrelas)
    op = input("Deseja gerar nova chave(S/N)?:")
  



