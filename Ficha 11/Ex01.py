# Biblioteca Tkinter: UI
from tkinter import *




# Variavel global com designacao do ficheiro
ficheiro = ".\\ficheiros\\texto.txt"


def guarda_ficheiro():
    """
    Guarda conteúdo da Text em ficheiro
    """
    linha = txtTexto.get("0.0","end-1c")    # end - 1 caracter (\n)
    fileText = open(ficheiro, "w", encoding="utf-8")
    fileText.write(linha)
    fileText.close()


# Limpa o conteúdo da Text
def limpar():
    """
    Limpa todo o conteúudo da Text
    """
    txtTexto.delete("0.0", "end")
   


 
def ler_ficheiro():
    """
    Le ficheiro de texto e ren deriza na Text
    """      
    fileText = open(ficheiro, "r", encoding="utf-8")
    lista = fileText.readlines()   # ler todo o ficheiro para uma lista
    fileText.close()
    
    limpar() # Limpa o conteúdo que eventualmente esteja na Text, para a seguir adicionar o conteudo do fx
    for linha in lista:
        txtTexto.insert("end", linha)
    


#---------------------------------------------------------------------    
class Application:
    def __init__(self, master=None):
        pass


# --- GUI DA APLICAÇÃO------------------------------------------------
window=Tk()                # invoca classe Tk , cria a "main window"
Application(window)        # Cria objeto window na classe Application
window.title('Exemplo')
#----------------------Exemplo para criar uma window centrada n screen
# Obtrer as dimensões do meu screen (em pixeis)
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appwidth = 700
appHeight = 400
x = (screenWidth/2) - (appwidth/2)
y= (screenHeight/2) - (appHeight/2)
window.geometry(f'{appwidth}x{appHeight}+{int(x)}+{int(y)}')


#Text 
txtTexto = Text(window, width = 55, height = 14, relief = "sunken", bd = 3)
txtTexto.place(x = 200, y= 50)

# Button Guardar
btnGuardar=Button(window,  text = "Guardar ficheiro" , width = 20, height = 2, fg = "blue",
                  command = guarda_ficheiro)
btnGuardar.place(x=20, y=50)

# Button Limpar
btnLimpar=Button(window,  text = "Limpar",width = 20, height = 2, fg = "blue",  
                command = limpar)
btnLimpar.place(x=20, y=150)

# Button Ler ficheiro
btnLer=Button(window,  text = "Ler ficheiro", width = 20, height = 2, fg = "blue", 
              command = ler_ficheiro)
btnLer.place(x=20, y=250)


window.mainloop()   # event listening loop by calling the mainloop()