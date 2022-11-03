#reverseWords - recebe um texto e inverte a ordem das palavras
def reverseWords(text):
    """
    it receives a string (text) 
    and returns the same text, with reversed words
    """
    newText=""
    pos = text.rfind(" ")   
    while pos != -1:
        newText+= text[pos+1:] + " "     # da posição a seguir ao espaço até ao fim
        text=text[0:pos]
        pos = text.rfind(" ")   
    newText+=text
    return newText

text = input("Texto:")
print(reverseWords(text))

input()