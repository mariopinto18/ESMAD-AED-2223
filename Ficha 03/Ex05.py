# Jogo Adivinha o número
# Dado um numero aleatorio, o utilizador deve adivinhá-lo
import os
import random

resposta = "S"
while resposta.upper == "S":
    os.system("cls")
    numero = random.randint(0,50)  # gera numro aleatorio entre 0 e 50

    print("\n" * 10)
    palpite = int(input("\t\t Indique o seu palpite: "))
    tentativas = 1
    while numero != palpite and tentativas <10:
    
        if palpite > numero:
            print("\t\t\t O número a adivinhar é MENOR \n")
        elif palpite < numero:
            print("\t\t\t O número a adivinhar é MAIOR \n")
        input()
        os.system("cls")
        print("\n" * 10)
        palpite = int(input("\t\t Indique o seu palpite: "))
        tentativas+= 1

    if numero == palpite:
        print("\t\t\t Parabéns! Acertou em {0} tentativas" .format(tentativas))
    else:
        print("\t\t\t Esgotou as 10 tentativas! :( ")

    ## Perguntar por novo Jogo
    resposta = input("Novo Jogo(S/N)? ")
print("Volte sempre...") 

