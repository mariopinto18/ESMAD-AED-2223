def standardName(name):
    """
    function receives a string text and returns the firt name, last name and 
    initials of middle names
    """
    newName=""
    # --------- primeiro nome
    pos = name.find(" ")             # 1º espaço
    if pos != -1:
        newName = name[:pos]        # obtem primeiro nome (até espaço)
    else:
        return "nome inválido!"
# --------- Iniciais dos nomes intermédios
    for i in range(pos, name.rfind(" ")):
        if name[i] == " ":
            newName+=  " " + name[i+1] + "."
    # ---------  ultimo nome
    pos = name.rfind(" ")               # 1º espaço a partir do fim
    if pos != -1:
        newName+= " " + name[pos+1:]    # obtem o ultimo nome
    
    return newName


name = input("Indique um nome:")
newName = standardName(name)
print(newName)
