# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import ttk          # treeview
from tkinter import filedialog   # filedialog boxes
import random                    # Nº aleatórios 
from tkinter import messagebox   #  messagebox



#Le ficheiro com perguntas do quizz. Gera nº aleatório para sortear questão.
# Coloca a pergunta e as hipoteses de resposta nos radiobuttons
def obter_questao(tema, resp1, resp2, resp3, resp4, cidade):
  """
  ficherio a ler as perguntas. depende do tema que está nas configurações (ficheiro perfil.txt)

  """
  ficheiro_perguntas = "ficheiros\\" + tema + ".txt"   
  f = open(ficheiro_perguntas, "r")
  lista_perguntas = f.readlines()
  f.close()

  numero = random.randint(0,len(lista_perguntas))   # sortear pergunta
  linha = lista_perguntas[numero]
  campos = linha.split(";")
  
  cidade.set(campos[0])
  resp1.config(text = campos[1], value = campos[1])
  resp2.config(text = campos[2], value = campos[2])
  resp3.config(text = campos[3], value = campos[3])
  resp4.config(text = campos[4], value = campos[4])
  global resp_certa
  resp_certa= campos[5]
 

def validar_resposta(resposta, respCertas, respErradas):
  """
  Valida se resposta dada (Radiobutton ativado) coincide com variável resp_certa 
  """
  mensagem = ""
  if resposta.get() == resp_certa:
    mensagem = "Parabéns, acertou!!!"
    respCertas.set(str(int(respCertas.get())+1))
  else:
     mensagem = "Errou esta pergunta!"
     respErradas.set(str(int(respErradas.get())+1))
  messagebox.showinfo(title = "Quizz", message = mensagem)


