# função que imprime number caracteres de texto por cada linha de impressão
def printCharLine(text, number):
    while (len(text)>number):   # enquanto o comprimento do texto > numero de caracteres a imprimir
        print(text[0:number])
        text=text[number:]
    print(text)



text = input("Texto:")
while True:
    try:
        number = int(input("Nº caracteres a imprimir por linha:"))
        if number <5 or number >12:
            raise ValueError()
    except ValueError:
        print(" O numero inserido não é valido. Tente novamente!")
    except:
        print("upss... ocorreu um erro!")
    else:
        break

printCharLine(text, number)

