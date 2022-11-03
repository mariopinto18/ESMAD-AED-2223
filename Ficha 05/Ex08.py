""" 
Função que recebe um texto e substitui a ocorrência de cada dígito decimal 
pelo seu nome em português
"""
def replaceNumbers(texto):
    """
    replace digits (between 0 and 9) by  
    """
    texto = texto.replace("0", "zero")
    texto = texto.replace("1", "um")
    texto = texto.replace("2", "dois")
    texto = texto.replace("3", "três")
    texto = texto.replace("4", "quatro")
    texto = texto.replace("5", "cinco")
    texto = texto.replace("6", "seis")
    texto = texto.replace("7", "sete")
    texto = texto.replace("8", "oito")
    texto = texto.replace("9", "nove")
    print(texto)



texto = input("Texto:")
replaceNumbers(texto)



