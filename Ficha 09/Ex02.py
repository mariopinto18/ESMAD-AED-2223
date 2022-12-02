import os


def cabecalho(data):
    os.system("cls")
    print("\n\n\t\tData da Consulta:", data)
    print()
    print()
    print("\t\t    Data     \t Hora   \tTemperatura")
    print("\t\t------------------------------------------")


# -------------------------- 
def consulta_data():
    os.system("cls")
    data = input("\n\n\t\tData da Consulta:")
    cabecalho(data)
    pagina=1
    lin = 1

    f = open(ficheiro, "r")
    linha = f.readline()   # ler 1º linha do fx
    while linha != '':    # Enq não chegar ao fim do ficheiro
        if lin == 11:      # imprime 11 linhas por cada página
            input("Pág. {0}. Prima <enter> para continuar" .format(pagina))
            pagina+=1
            lin=1
            cabecalho(data)      
        campos = linha.split(";")    # cada linha da lista é dividida em 3 partes, pelos ";"
        if campos[0] == data:   # se data de consulta  == campos[0]
            print("\t\t", campos[0], "\t", campos[1], "\t", campos[2])
            lin+=1
        linha = f.readline()
    f.close()
    input()




# Consulta de dados estatísticos
def consulta_estatistica():
    temp = []
    f = open(ficheiro, "r")
    linha = f.readline()            # ler 1º linha do fx
    while linha != '':
        campos = linha.split(";")   # divide cada linha proveniente do fx pelos ";"
        temperatura = int(campos[2])
        temp.append(temperatura)    # faz o append da temperatura a uma lista só com temperaturas
        linha = f.readline()        # ler as linhas eguintes do fx
    f.close()
    
    maximo = max(temp)
    minimo = min(temp)
    media = sum(temp)/ len(temp)
    print("\n\n\n\tO maior valor de temperatuar registada foi de {0}" .format(maximo))
    print("\n\tO menor valor de temperatuar registada foi de {0}" .format(minimo))
    print("\n\tO valor médio de temperatuar registada foi de {:.2f}" .format(media))
    input()

# ----- Inicio do programa -------
ficheiro = "temperatura.txt"
op = 1
while op != 0:
    os.system("cls")
    print("\n\nMENU")
    print("1 - Consulta por data")
    print("2 - Consulta Estatistica")
    print("0 - Sair")
    op = int(input("\t opção: "))
    if op ==1:
        consulta_data()
    elif op ==2:
        consulta_estatistica()

