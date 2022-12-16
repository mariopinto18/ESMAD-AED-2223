# Biblioteca Tkinter: UI
from tkinter import *



def PesoIdeal():
    """
    Detrermina o peso ideal em função do genero e altura
    """
    k=4
    if genero.get() == "Masculino":
        k=4
    else:
        k=2
    # Obter valor da Entry altura: altura.get()
    peso = (altura.get() - 100) - (altura.get() - 150)/k
    pesoIdeal.set(str(peso))
    

#----------------------------------------------------------------------
class Application:
    def __init__(self, master=None):
        pass

# --- GUI DA APLICAÇÃO------------------------------------------------
window=Tk()                # invoca classe Tk , cria a "main window"
Application(window)        # Cria objeto window na classe Application
window.title('Peso Ideal')
#----------------------Exemplo para criar uma window centrada n screen
# Obtrer as dimensões do meu screen (em pixeis)
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appwidth = 700
appHeight = 300
x = (screenWidth/2) - (appwidth/2)
y= (screenHeight/2) - (appHeight/2)
window.geometry(f'{appwidth}x{appHeight}+{int(x)}+{int(y)}')


#Label
lblAltura=Label(window, text="Altura em cm:", fg="blue", font=("Helvetica 9 bold") )
lblAltura.place(x=25, y=30)
#Entry
altura = IntVar()
txtAltura=Entry(window, width = 10, textvariable = altura)
txtAltura.place(x=120, y=30)

#Frame
lFrame = LabelFrame(window, width = 300, height=130, bd=3, text= "Género", fg = "blue", relief = "sunken")
lFrame.place(x=25, y=100)
#Radiobutton
genero = StringVar()
genero.set("Masculino")   # Opção selecionada por defeito
rd1 = Radiobutton(lFrame, text = "Masculino", value = "Masculino", variable = genero)
rd1.place(x=15, y=20)
rd2 = Radiobutton(lFrame, text = "Feminino", value = "Feminino", variable =  genero)
rd2.place(x=15, y=50)

#Button
btnPesoIdeal=Button(window,  text = "Calcular \nPeso Ideal" , width = 15, height = 5, 
                            relief = "raised",fg = "blue",  command = PesoIdeal)
btnPesoIdeal.place(x=330, y=125)


# Panel
panel1 = PanedWindow(window, width = 230, height = 120, bd = "3", relief = "sunken")
panel1.place(x=450, y=110)

lblPesoIdeal=Label(panel1, text="Peso Ideal em Kg",  fg="blue", font=("Helvetica", 9))
lblPesoIdeal.place(x=42, y=25)
#Entry
pesoIdeal=StringVar()
txtPesoIdeal=Entry(panel1, width = 15, state = "disabled" , textvariable = pesoIdeal)
txtPesoIdeal.place(x=59, y=60)

window.mainloop()   # event listening loop by calling the mainloop()