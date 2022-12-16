# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import messagebox


ficheiro = "tarefas.txt"

class Application:
    def __init__(self, master=None):
        pass



def numTarefas():
    cont = lboxTarefas.size()
    countTarefas.set(str(cont))


def adicionar():
    """
    Adiciona uma tarefa à ListBox, a partir da Entry tarefa
    """
    lboxTarefas.insert("end", tarefa.get())
    tarefa.set("") 
    numTarefas()


def limpar():
    """
    Limpa a Listbox
    """
    lboxTarefas.delete(0, "end")
    numTarefas()


def remover():
    """
    remove uma tarefa da lista
    """
    pos = lboxTarefas.curselection()   # obtem o índice da linha ativa 
    #                                 / OU: lboxTarefas.focus()
    if len(pos) >0:
       # Remove o item selecionado da Listbox
        lboxTarefas.delete(lboxTarefas.curselection())   # indice do item selecionado
        tarefa.set("")
        numTarefas()
    else:
        messagebox.showerror("info", "Não existem dados selecionados")




def selecao_item(event):
    indice = lboxTarefas.curselection()   # Índice da linha selecionada
    texto = lboxTarefas.get(indice)       # Obter conteudo da Listbox, linha selecionada 
    tarefa.set(texto)


def guardar_fx():
    """
    Guardar lista de tarefas em file
    """
    fileTarefas = open(ficheiro, "w", encoding="utf-8")
    cont = lboxTarefas.size()                   # conta nº d etarefas na ListBox
    for i in range(cont):                       # Iterar tarefas
           atividade = lboxTarefas.get(i)       # Obter cada uma das tarefas da ListBox 
           if atividade.find("\n") == -1:
               atividade = atividade + "\n"
           fileTarefas.write(atividade)         # Guarda em ficheiro
    fileTarefas.close()  



def ler_fx():
    """
    Upload de ficheiro d etarefas
    """
    limpar()
    fileTarefas = open(ficheiro, "r", encoding="utf-8")
    lista  =fileTarefas.readlines()
    fileTarefas.close()
    for linha in lista:
        lboxTarefas.insert("end", linha)
    numTarefas()   


def ordenar():
    """
    Ordenar lista de tarefas
    """
    cont = lboxTarefas.size()     # Nº tarefas na ListBox
    lista=[]                       # Lita vazia
    for i in range(cont):          # carrega lista a partir da Listbox
        lista.append(lboxTarefas.get(i)) 
    lista.sort()                    # Ordena
    lboxTarefas.delete(0, "end")   # apaga conteudo da Listbox
    for linha in lista:             # coloca lista ordenada na Listbox
        lboxTarefas.insert("end", linha)




# --- GUI DA APLICAÇÃO------------------------------------------------
window=Tk()                # invoca classe Tk , cria a "main window"
Application(window)        # Cria objeto window na classe Application
window.title('ToDoList')
#----------------------Exemplo para criar uma window centrada n screen
# Obtrer as dimensões do meu screen (em pixeis)
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

appwidth = 700
appHeight = 400
x = (screenWidth/2) - (appwidth/2)
y= (screenHeight/2) - (appHeight/2)
window.geometry(f'{appwidth}x{appHeight}+{int(x)}+{int(y)}')



#Panel para ListBox
panel1 = PanedWindow(window, width = 250, height = 300, bd = "3", relief = "sunken")
panel1.place(x=10, y=30)

#ListBox
lboxTarefas=Listbox(panel1, width = 35, height=15, bd="3", selectmode = "single",
                     selectbackground="orange")
lboxTarefas.place(x=8, y= 25)
#lboxTarefas.bind("<<ListboxSelect>>", selecao_item)      # Evento ao selecionar item da Listbox #########


# Panel tarefa
panel2 = PanedWindow(window, width = 350, height = 100, bd = "3", relief = "sunken")
panel2.place(x=300, y=30)
#Label
lbl_tarefa=Label(panel2, text="Tarefa:", fg="blue", font=("Helvetica", 9))
lbl_tarefa.place(x=20, y=30)
#Entry
tarefa = StringVar()
txtTarefa=Entry(panel2, width = 35, textvariable= tarefa)
txtTarefa.place(x=80, y=30)

# Buttons
btnAdd=Button(window,  text = "Adicionar" , width = 12,height = 2, fg = "black", command = adicionar)
btnAdd.place(x=300, y=200)

btnRemove=Button(window,  text = "Remove",width = 12, height = 2, fg = "black", command = remover )
btnRemove.place(x=400, y=200)

btnClear=Button(window,  text = "Clear", width = 12, height = 2, fg = "black", command = limpar)
btnClear.place(x=500, y=200)

btnUpload=Button(window,  text = "Upload" , width = 12,height = 2, fg = "black", command= ler_fx)
btnUpload.place(x=300, y=260)

btnDownload=Button(window,  text = "Download",width = 12, height = 2, fg = "black", command = guardar_fx)
btnDownload.place(x=400, y=260)

btnOrd=Button(window,  text = "Ordenar", width = 12, height = 2, fg = "black", command = ordenar)
btnOrd.place(x=500, y=260)

# Numero de Tarefas pendentes:
#Label
lblCount_tarefas=Label(window, text="Nº de Tarefas Pendentes:", fg="blue", font=("Helvetica", 9))
lblCount_tarefas.place(x=300, y=340)
#Entry
countTarefas = StringVar()    # variavek associada à Entry contadora de tarefas
txtCountTarefas=Entry(window, width = 5, textvariable= countTarefas, state="disabled")
txtCountTarefas.place(x=450, y=340)


window.mainloop()   # event listening loop by calling the mainloop()