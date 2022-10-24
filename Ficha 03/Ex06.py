# gera um ano e verifica se é bissexto ou não

import random

resposta = "S"
while resposta == "S":
    ano = random.randint(1900,2020)
    print(ano)
    # Multiplo de 400 => bissexto
    # Multiplo de 4 mas não multiplo de 100 => bissexto
    # Em todas as outras situações, não é bissexto
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        print("o ano {0} é bissexto" .format(ano))
    else:
        print("o ano {0} não é bissexto" .format(ano))

    resposta = input("Gerar novo ano(S/N)? ")
