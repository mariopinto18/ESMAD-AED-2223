# Biblioteca Tkinter: UI
from tkinter import *



def calcular_imc():
    """
    calcula IMC com base na altura e do peso
    """
    altura_M = altura.get() /100        # obter altura da Entry e converter e metros
    imc = peso.get() / (altura_M * altura_M)
    str_imc = "{0:.2f}".format(imc)    # Formata com 2 casas decimais
    val_imc.set(str_imc)               # colocar imc na variável associada à label


def sair():
  """
  opção de sair, terminar
  """
  # window.quit()     # fecha o container window
  window.destroy()    # fecha e remove da memoria 



#-------------------------------------------
class Application:
    def __init__(self, master=None):
        pass



# --- GUI DA APLICAÇÃO------------------------------------------------
window=Tk()                # invoca classe Tk , cria a "main window"
Application(window)        # Cria objeto window na classe Application
window.title('Simulador IMC')
#----------------------Exemplo para criar uma window centrada n screen
# Obtrer as dimensões do meu screen (em pixeis)
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appwidth = 750
appHeight = 350
x = (screenWidth/2) - (appwidth/2)
y= (screenHeight/2) - (appHeight/2)
window.geometry(f'{appwidth}x{appHeight}+{int(x)}+{int(y)}')


# ----- painel 1
panel1 = PanedWindow(window, width = 250, height = 150, bd = "3", relief = "raised")
panel1.place(x=50, y=40)

#Label
lbl_peso=Label(panel1, text="Peso   :", fg="blue", font=("Helvetica", 9))
lbl_peso.place(x=25, y=30)

lbl_altura=Label(panel1, text="Altura (cm):", fg="blue", font=("Helvetica", 9))
lbl_altura.place(x=25, y=70)
#Entry
peso = IntVar()
txt_peso=Entry(panel1, width = 10, textvariable=peso)
txt_peso.place(x=120, y=30)

altura = IntVar()
txt_altura=Entry(panel1, width = 10, textvariable=altura)
txt_altura.place(x=120, y=70)

# ----- painel 2
panel2 = PanedWindow(window, width = 250, height = 120, bd = "3", relief = "raised")
panel2.place(x=50, y=200)

lbl_imc_text = Label(panel2, text = "Índice de Massa Corporal", font = ("Helvetica", 10), fg = "blue")
lbl_imc_text.place(x=25, y=4)

val_imc = StringVar()           # variavel associada à label que mostra o resultado
lbl_imc = Label(panel2,  fg = "red", textvariable = val_imc, font = ("Helvetica, bold", 12))
lbl_imc.place(x=65, y=50)

#2 Buttons
btn_PesoIdeal=Button(window,  text = "Calcular \nIMC" , width = 10, height = 4, relief = "raised", fg = "black", command = calcular_imc)
btn_PesoIdeal.place(x=350, y=70)

btn_PesoIdeal=Button(window,  text = "Sair" , width = 10, height = 4, relief = "raised", fg = "black", command=sair)
btn_PesoIdeal.place(x=350, y=150)

# ------- Imagem
# container Canvas, usado para aplicações de desenho: imagens e formas geométricas
ctn_canvas = Canvas(window, width = 270, height = 180, bd = 2, relief = "sunken")
ctn_canvas.place(x=470, y=40)

img = PhotoImage(file = "imc.gif")
ctn_canvas.create_image(135,90, image = img)



window.mainloop()   # event listening loop by calling the mainloop()