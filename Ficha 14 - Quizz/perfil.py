
# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import ttk          # treeview
from tkinter import filedialog   # filedialog boxes
#import random                    # Nº aleatórios 
import os
from tkinter import messagebox   #  messagebox

ficheiro_perfil = "ficheiros\\perfil.txt"


def guardarPerfil(continente, filename):
  """
  Guarda dados no ficheiro perfil.txt
  """
  filePerfil = open(ficheiro_perfil, "w")
  global tema
  tema = str(continente.get())
  linha = filename + ";" + tema     # Imagem d eperfil;tema selecionado
  filePerfil.write(linha)
  filePerfil.close()
 
  


def ler_perfil():
  """
  Ler ficheiro de perfil: devolve nome do ficheiro associado à imagem de perfil, assim como o tema predefinido 
  """
  if not os.path.exists(ficheiro_perfil):
      filePerfil = open(ficheiro_perfil, "w")
      filePerfil.write("imagens\avatar0.png;Europa")
      filePerfil.close
  filePerfil = open(ficheiro_perfil, "r")
  linha= filePerfil.readline()
  filePerfil.close()

  filename =  linha.split(";")[0]
  tema = linha.split(";")[1]
  return filename, tema

