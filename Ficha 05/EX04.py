# Função que substitui 2 ou mais espaços por um único espaço
def removeSpaces(text):
    """
    function receives a string and replaces 2 or more spaces with a single space
    """
    while text.find("  ")!= -1 :          # Enquanto encontrar sequências de 2 espaços
        text = text.replace("  ", " ")    # substituir 2 espaços por 1
    print("Texto:",text)


    
text = input("Insira um Texto:") 
removeSpaces(text)
