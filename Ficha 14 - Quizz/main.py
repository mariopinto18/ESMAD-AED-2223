# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import ttk          # treeview
from tkinter import filedialog   # filedialog boxes
#import random                    # Nº aleatórios 
import os
#from tkinter import messagebox   #  messagebox
from jogar import *
from perfil import *




def atualizaImgPerfil():
  """
  atualiza canvas de imagem de perfil no PanelUser (HEADER), com imagem guardada em ficheiro
  """
  global imgPerfilHeader
  global imageHeader_id
  imgPerfilHeader = PhotoImage(file = filename)
  ctnUser.itemconfig(imageHeader_id, image=imgPerfilHeader)




def selecionaPerfil():
  """
  selecionar imagem para o perfil, nas configurações, a partir de FileDialog
  """
  global filename
  filename = filedialog.askopenfilename(title = "Select file", initialdir= "./imagens",
              filetypes = (("png files","*.png"),("gif files", "*.gif"), ("all files","*.*")))
  
  global img_perfil
  global image_perfil_id
  img_perfil = PhotoImage(file = filename)
  # change image on canvas
  global canvas_perfil
  canvas_perfil.itemconfig(image_perfil_id, image=img_perfil)



def PanelConfigurar():
    # ------------------------------------------------------------
    panelConfig = PanedWindow(window, width = 700, height = 450, bd = "3", relief = "sunken")
    panelConfig.place(x=0, y=50)

    btn_selecionar = Button(panelConfig, text = "Selecione imagem \nde perfil", width = 14, height = 3, 
                    command = selecionaPerfil)

    btn_selecionar.place(x=100, y= 70)
    global canvas_perfil
    canvas_perfil = Canvas(panelConfig, width = 50, height = 50, bd = 4, relief = "sunken")
    canvas_perfil.place(x=270, y=70)
    global img_perfil, filename
    img_perfil = PhotoImage(file = filename)
    global image_perfil_id
    image_perfil_id = canvas_perfil.create_image(25, 25, image=img_perfil)

    frame1 = LabelFrame(panelConfig, text = "Selecione o continente para jogar", width = 300, height = 150, bd = 3, relief = "sunken")
    frame1.place(x=100, y=150)
    continente = StringVar() 
    rb1 = Radiobutton(frame1, text = "Europa",  variable = continente, value = "Europa")
    rb2 = Radiobutton(frame1, text = "America", variable = continente, value = "America")
    rb3 = Radiobutton(frame1, text = "Asia",    variable = continente, value = "Asia")
    if tema != "":
       continente.set(tema)
    else:
       continente.set("Europa")
    rb1.place(x=10, y= 20)
    rb2.place(x=10, y= 50)
    rb3.place(x=10, y= 80)

    #---- GUARDAR configurações
    btn_guardar = Button(panelConfig, text = "Guardar configurações", height = 3, width=42, 
                    command = lambda: [guardarPerfil(continente, filename),  atualizaImgPerfil()])
    btn_guardar.place(x=100, y=320)



def panelJogar():
    # Panel Jogar  -------------------------------------
  panelJogar = PanedWindow(window, width = 700, height = 450, relief = "flat" )
  panelJogar.place(x=0, y=50)


  lb1 = Label(panelJogar, text = "Cidade", font = ("Helvetica", "15"))
  lb1.place(x=290, y=30)

  cidade = StringVar()
  cidade.set("")
  txtCidade = Entry(panelJogar, textvariable =cidade, width = 25, state = "disabled", font = ("Helvetica", "12"))
  txtCidade.place(x=230, y=60)

  frame2 = LabelFrame(panelJogar, text = "É a Capital do país:", width = 450, height = 150, bd = 3, relief = "sunken")
  frame2.place(x=120, y=100)
  resposta = StringVar(frame2, "A")   # variavel que contém o conteudo / valor do radiobutton selecionado
  resp1 = Radiobutton(frame2, text = "Opção A", variable = resposta, value = "A", font = ("Helvetica", "10"))
  resp2 = Radiobutton(frame2, text = "Opção B", variable = resposta, value = "B", font = ("Helvetica", "10"))
  resp3 = Radiobutton(frame2, text = "Opção C", variable = resposta, value = "C", font = ("Helvetica", "10"))
  resp4 = Radiobutton(frame2, text = "Opção D", variable = resposta, value = "D", font = ("Helvetica", "10"))

  resp1.place(x=20, y= 20)
  resp2.place(x=250, y= 20)
  resp3.place(x=20, y= 100)
  resp4.place(x=250, y= 100)

  global btnImage1, btnImage2
  btnImage1 = PhotoImage(file = "imagens\\icoPergunta.png")
  btnNovaPergunta = Button(panelJogar, text = "Nova Pergunta", image = btnImage1, compound = LEFT, 
                        width = 220, height = 48, font = ("Helvetica", "10"),
                        command =lambda: obter_questao (tema, resp1, resp2, resp3, resp4, cidade))
  btnNovaPergunta.place(x=120, y=280)
  
  btnImage2 = PhotoImage(file = "imagens\\icovalidar.png")
  btnResponder = Button(panelJogar, text = "Validar Resposta", image = btnImage2,compound = LEFT,  
                      width = 220, height = 48, font = ("Helvetica", "10"),  command = lambda: validar_resposta(resposta, respCertas, respErradas))
  btnResponder.place(x=340, y=280)


  panelRespostas = PanedWindow(panelJogar, width = 700, height=50, relief="sunken")
  panelRespostas.place(x=0, y= 400)
  lblCertas = Label(panelJogar, text = "Acertou:")
  lblCertas.place(x=100, y=410)
  respCertas = StringVar()
  respCertas.set("0")
  lblrespCertas = Label(panelJogar, textvariable= respCertas, state="disabled", width=3)
  lblrespCertas.place(x=180, y=410)

  lblErradas = Label(panelJogar, text = "Errou:")
  lblErradas.place(x=500, y=410)
  respErradas = StringVar()
  respErradas.set("0")
  lblRespErradas = Label(panelJogar, textvariable= respErradas, state="disabled", width=3)
  lblRespErradas.place(x=580, y=410)



# ---------------Main---------------------
#-----------------------------------------
window = Tk()
screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()
appWidth = 700                             # tamanho (pixeis) da window a criar 900 / 500
appHeight = 500 
x = (screenWidth/2) - (appWidth/2)        # posição do canto superior esquerdo da window
y = (screenHeight/2) - (appHeight/2)
window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}" .format(appWidth, appHeight, int(x), int(y)))
window.title('Quizz - Capitais')


ficheiro_perfil = "ficheiros\\perfil.txt"
filename, tema = ler_perfil()


PanelStatus = PanedWindow(window, width=700, height=50, relief = "flat")
PanelStatus.place(x=0, y=0)

#----- Button JOGAR ------------------------------
imageNovo = PhotoImage(file = "imagens\\icoNovo.png" )
btnJogar = Button(PanelStatus, text = "Novo Jogo", width = 100, height = 48, image = imageNovo, compound = LEFT,
                   font = ("Helvetica", "10"),  command = panelJogar)
btnJogar.place(x=100, y=0)
#----- Button SAIR ------------------------------
imageSair = PhotoImage(file = "imagens\\icoSair.png" )
btnSair = Button(PanelStatus, text = "Fechar", width = 100, height = 48,   image = imageSair, compound = LEFT,
                  font = ("Helvetica", "10"),  command = window.destroy)
btnSair.place(x=250, y=0)
#----- Button CONFIGURAÇÕES -----------------------
imageConfig = PhotoImage(file = "imagens\\icoConfig.png" )
btnConfig = Button(PanelStatus, text = "Configurar \nopções", image = imageConfig, compound = LEFT, 
                  width = 100, height = 48, font = ("Helvetica", "10"), command = PanelConfigurar)
btnConfig.place(x=400, y=0)
# Imagem de perfil
ctnUser = Canvas(PanelStatus, width = 50, height = 50, relief = "flat")
ctnUser.place(x=600, y=0)
imgPerfilHeader = PhotoImage(file = filename)
imageHeader_id = ctnUser.create_image(25, 25, image=imgPerfilHeader)


# ------------ Imagem do Quizz ------------------
ctnLogo = Canvas(window, width = 700, height = 450, relief = "flat")
ctnLogo.place(x=0, y=70)
img_logo = PhotoImage(file = "imagens\\quizzCapitais.png")
ctnLogo.create_image(350, 225, image=img_logo)

window.mainloop()   # event listening loop by calling the mainloop()