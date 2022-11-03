# função que recebe um texto e devolve o primeiro e último nome 
def shortName(name):
    """
    function receives a string text and returns the firt and last names
    """
    newName=""
    pos = name.find(" ")                # 1º espaço
    if pos != -1:
        fisrt_name = name[:pos]         # obtém o 1º nome (até ao espaço)
        pos = name.rfind(" ")           # ultimo espaço
        if pos != -1:
            last_name = name[pos+1:]    # Obtém o ultimo nome (do espaço até ao fim)
            newName = fisrt_name+" " + last_name
            return newName
    return "nome inválido"     # no caso de não ter feito o return  na linha anterior


name = input("Nome:")
print(shortName(name))


