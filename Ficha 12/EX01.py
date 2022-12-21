# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import ttk # treeview
from tkinter import messagebox 
import datetime
import os
from tkinter import filedialog

# path do ficheiro
ficheiro = ".\\files\\presencas.txt"



def consulta():
    """
    renderiza window da opção Consulta de movimentos
    """
    conWindow = Toplevel()
    conWindow.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
    conWindow.title("Consultas")
    conWindow.focus_force()  # força o focus na window atual
    conWindow.grab_set()    # direciona todos os eventos para a window ativa 

    # Panel
    panel1 = PanedWindow(conWindow, width = 200, height = 270, bd = "3", relief = "sunken")
    panel1.place(x=15, y=20) 
    #Frame Tipo de Movimento - checkbuttons para entradas / saídas
    lframe = LabelFrame(panel1, width = 160, height=100, bd=3, text= "Tipo de Movimento", fg = "blue", relief = "sunken")
    lframe.place(x=5, y=5)
    # CheckButtons
    cb1 = IntVar()
    cb2 = IntVar()
    ck1 = Checkbutton(lframe, text = "Entrada", variable = cb1)
    ck1.place(x=15, y=15)
    ck2 = Checkbutton(lframe, text = "Saída", variable = cb2)
    ck2.place(x=15, y=40)
    #Frame Utilizador    - entry para indocar nº de utilizador a consultar
    lframe2 = LabelFrame(panel1, width = 160, height=100, bd=3, text= "Por Utilizador", fg = "blue", relief = "sunken")
    lframe2.place(x=5, y=120)
    # Label
    lblUtilizador = Label(lframe2, text="Número: ")
    lblUtilizador.place(x=15, y=5)
    #Entry    
    utilizador = StringVar()
    txtUtilizador = Entry(lframe2, width = 15, textvariable = utilizador)
    txtUtilizador.place(x=15, y=25)
    #  Button consultar dados
    btnConsultar = Button(panel1, width = 21, height= 2, text = "Consultar", 
                        relief = "raised", command = lambda: consultaMovimentos(cb1, cb2, utilizador, tree))
    btnConsultar.place(x=8, y=222)

    # Painel 2
    panel2 = PanedWindow(conWindow, width = 460, height = 270, bd = "3", relief = "sunken")
    panel2.place(x=220, y=20)
    # TreeView para consulta de movimentos
    tree = ttk.Treeview(panel2, height = 11, selectmode = "browse", columns = ("Número", "Data", "Hora", "Movimento"), show = "headings")
 
    tree.column("Número", width = 100,   anchor="c")
    tree.column("Data", width = 100,  anchor="c")          # c- center, e - direita, w- esquerda
    tree.column("Hora", width = 100,   anchor="c")
    tree.column("Movimento", width = 140,   anchor="c")
    tree.heading("Número", text = "Número")
    tree.heading("Data", text = "Data")
    tree.heading("Hora", text = "Hora")
    tree.heading("Movimento", text = "Movimento")
    tree.place(x=5, y=5)




def consultaMovimentos(cb1, cb2, utilizador, tree):  
    """
    Consulta movimentos em Treeview, de acordo com filtros selecionados
    """
    tree.delete(*tree.get_children()) 
    mov = ""
    if cb1.get() == True and cb2.get() == True:   # Se está checado entrada e saída (cb1 e cb2)
        mov = "T"
    else:
        if cb1.get() == True:                      # se está apenas checado cb1 (entrada)
            mov = "Entrada\n"
        if cb2.get() == True:                      # se está apenas checado cb2 (saida)
            mov = "Saída\n"
    fileAcessos = open(ficheiro, "r", encoding="utf-8")
    lista = fileAcessos.readlines()
    fileAcessos.close()
    for linha in lista:
        campos = linha.split(";")
        if mov == "T" or  campos[3] == mov:
            if utilizador.get() == "" or utilizador.get() == campos[0]:
                    tree.insert("", "end", values = (campos[0], campos[1], campos[2], campos[3]))


#------------------------------------------------------------

def validoMov(selected, numero):

    global listaMov
    for i in range(len(listaMov)-1, -1, -1):
        linha = listaMov[i]
        fields = linha.split(";")
        if fields[0] == str(numero.get()):    # ENCONTROU o mesmo nº aluno
            if selected.get() == fields[3][:-1]:
                return False
            else:
                return True
    return True



def registarMov(selected, numero, lboxMov):
    """
    Registar movimento em ficheiro
    """
    if not validoMov(selected, numero):
        messagebox.showerror("Gestão Presenças", "O movimento não é permitido")
        return
    # Regista movimento em ficheiro
    data =  str(datetime.date.today())
    hora = str(datetime.datetime.now().time().strftime("%H:%M:%S"))
    linha = str(numero.get())  + ";" + data + ";" + hora + ";" + selected.get() + "\n"
    fileAcessos = open(ficheiro, "a", encoding="utf-8")
    fileAcessos.write(linha)
    fileAcessos.close()
    lboxMov.insert("end", linha)    # Acrescenta à Listbox de nmovimentos
    
    global listaMov
    listaMov.append(linha)          # Adiciona â lista interna de movimentos



def movFicheiro():
    """
    Lista com movimentos existentes em ficheiro
    """
    listaMov = []
    if os.path.exists(ficheiro):   # Ficheiro existe
        fileAcessos = open(ficheiro, "r", encoding="utf-8")
        listaMov = fileAcessos.readlines()
        fileAcessos.close()    
    return listaMov
   

def movimentos():
    """
    renderiza container de movimentos - entradas e saídas
    """
    movWindow = Toplevel()   # Objeto da classe Toplevel, janela principal
    movWindow.title("Entradas e Saídas") 
    movWindow.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
    movWindow.focus_force()  # força o focus na window atual
    movWindow.grab_set()        # Força que todos os eventos (p.e. clicar num button)  estejam enquadrados no componente atual (janela top)
             
    lblNumero = Label(movWindow, text="Número de Estudante:")
    lblNumero.place(x=20, y=15)
    # Entry
    numero = IntVar()
    txtNumero = Entry(movWindow, width = 20, textvariable = numero)
    txtNumero.place(x=150, y=15)
    # LabelFrame
    lframe = LabelFrame(movWindow, width = 200, height=130, bd=3, text= "Movimentos", fg = "blue", relief = "sunken")
    lframe.place(x=25, y=60)
    #RadioButton
    selected = StringVar()
    rd1 = Radiobutton(lframe, text = "Entrada", value = "Entrada", variable = selected)
    rd1.place(x=15, y=20)
    rd2 = Radiobutton(lframe, text = "Saída", value = "Saída", variable = selected)
    rd2.place(x=15, y=50)
    selected.set("Entrada")   # Opção selecionada por defeito 
    #Button
    btnRegistar = Button(movWindow, width = 12, height= 4, text = "Registar", 
                    command = lambda: registarMov(selected, numero, lboxMov))
    btnRegistar.place(x=250, y=80)
    # Label movimentos
    lblHistorico = Label(movWindow, text="Histórico de movimentos", fg = "blue", font = ("Helvetica, 10"))
    lblHistorico.place(x=460, y=15)
    #ListBox
    lboxMov =Listbox(movWindow, width = 40, height=10, bd="3", selectmode = "single")
    lboxMov.place(x=420, y= 60)




listaMov = movFicheiro()  ## carrega ficheiro para lista

#-----Arranque da aplicação --------------------------------
#----------------------------------------------------------
window=Tk()   # invoca classe tk , cria a "main window"

#Get the current screen width and height
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appWidth = 700                             # tamanho (pixeis) da window a criar
appHeight = 300
x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))

window.title('Gestão de Presenças')

barraMenu = Menu(window)
# Constroi menu Simuladores, com 2 opções dropd-down
barraMenu.add_command(label = "Movimentos",command = movimentos)
barraMenu.add_command(label = "Consulta",command = consulta)
# Constroi menu Sair, com comando quit
barraMenu.add_command(label = "Sair", command = window.destroy)     # OU window.quit
window.configure(menu=barraMenu)

lbl = Label(window, text = "Gestão \nde \nPresenças", fg = "blue", font = ("Helvetica", 16))
lbl.place(x=500, y=120)
# ------- Imagem
# container Canvas, usado para aplicações de desenho: imagens e formas geométricas
ctnCanvas = Canvas(window, width = 450, height = 300, bd = 1, relief = "flat")
ctnCanvas.place(x=0, y=0)

img = PhotoImage(file = ".\images\\presencas.png")
ctnCanvas.create_image(223,150, image = img)


# EDITAR LABELS DE MENU
#barraMenu.entryconfigure(1, label = "UM")
#barraMenu.entryconfigure(2, label = "DOIS")


window.mainloop()   # event listening loop by calling the mainloop()
