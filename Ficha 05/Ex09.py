
# Função que o nº de ocorrência de uma palavra, num texto
def countWord(text, txtFind):
    """
    It receives a string text, and a string word to find 
    It returns de number of occurences and positions
    """
    text = " " + text + " "
    txtFind = " " + txtFind + " "
    num = text.count(txtFind)     # nº de ocorrencias

    ant=0           
    positions=""     # variável de saida com as diversas posições no texto
    for i in range(num):
        pos = text.find(txtFind, ant) # pesquisa (find) no texto a partir da posição ant
        if pos != -1:
            positions+= " " + str(pos+1)   
            ant = pos + 1
        else:
            break
    return num, positions     # devolve nº ocorrencias (num) e posições (positions)

text = input("Texto:")
txtFind = input("Pesquisa:")
num, positions = countWord(text, txtFind)
print("A palavra {0} ocorre {1} vezes no texto. Nas posições {2}" .format(txtFind, num, positions))




