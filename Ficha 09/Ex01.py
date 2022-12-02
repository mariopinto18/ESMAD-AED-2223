import os




def cabecalho():
    os.system("cls")
    print()
    print()
    print("\t\t    País     \t Continente")
    print("\t\t------------------------------------------")


#------------------------------------
def consulta(continente):
    """
    It shows the countries of a continent
    """
    cabecalho()
    pagina=1
    lin = 1         # conta o nº de linhas a imprimir em cada tela
 
    if not os.path.isfile(ficheiro):
        print("O ficheiro de países não existe!")
        return
    fpaises = open(ficheiro, "r", encoding="utf-8")
    linhas = fpaises.readlines()
    fpaises.close()

    for linha in linhas:
        if lin == 11:
            input("Pág. {0}. Prima <enter> para continuar" .format(pagina))
            pagina+=1           # contador de páginas da consulta
            lin=1               # contador de linhas por página da consulta
            cabecalho() 
        campos = linha.split(";")
        if continente == '' or continente == campos[1][:-1]:
            if len(campos[0]) < 6:
                campos[0]+= "\t"
            print("\t\t", campos[0], "\t\t", campos[1])
            lin+=1              # conta o nº de linhas a imprimir em cada tela
 
    input()

#------------------------------
def paisExiste(pais):
    """
    Boolean function, checks if pais already exists in the file
    """
    if os.path.exists(ficheiro) == False:   # Se o ficheiro NÂO existe
        return False
    fpaises = open(ficheiro, "r", encoding="utf-8")
    listaPaises = fpaises.readlines()   # carrega todo o ficheiro para uma lista denominada paises
    fpaises.close()

    for linha in listaPaises:           # percorre toda a lista paises
        if pais == linha.split(";")[0]:
            return True
    return False            # se chegou ao fim do for e nunca devolveu True, é pq o pais não existe no ficheiro



def guardaFicheiro(pais, continente):
    """
    Save in file the contry and continent
    """
    linha = pais + ";" + continente + "\n"
    fpaises = open(ficheiro, "a", encoding="utf-8")   # Abre fx em modo "append"
    fpaises.write(linha)                              # guarda em ficheiro 
    fpaises.close()                                   # fecha ficheiro



def insercao():
    """
    It inserts a new country into the file. If it already exists in the file, it shows a message
    """    
    os.system("cls")
    pais = input("\n\n\n\n\t\tPaís       : ")
    continente = input("\n\t\tContinente : ")
    if continente not in lcontinentes:
        print("Esse continente não existe na lista de continentes autorizados!")
        input()
        return
    if paisExiste(pais):
        print("\n\nO país {0} já existe no ficheiro! Prime <enter> para continuar..." .format(pais))
        input()
    else:
        guardaFicheiro(pais, continente)




# Variáveis globais do programa, que definem o nome da pasta e do ficheiro (path incluida)
pasta = "files"
ficheiro = ".\\files\paises.txt"
# Lista de continentes válidos
lcontinentes = ['Europa', 'Asia', 'America', 'Africa', 'Oceania']

# se a pasta files não existe, cria a pasta
if not os.path.exists(pasta):
    os.mkdir(pasta)
#----------------------------------------

op = "1"
while op != "0":
    os.system("cls")
    print("\n\nMENU")
    print("1 - Inserir Países")
    print("2 - Consulta Países")
    print("3 - Consulta por continente")
    print("4 - Consulta nº países")
    print("0 - Sair")
    op = input("\t opção: ")
    if op =="1":
        insercao()          # Inserção de dasdos: país e continente
    elif op=="2":           # Consulta geral
        consulta('')
    elif op =="3":          # Consulta por continente
        os.system("cls")
        continente = input("\n\n\t\tContinente: ")
        consulta(continente)
    elif op == "4":         # Consulta nº países por continente
        consulta()
print("\n\nObrigado, volte sempre... :-) ")