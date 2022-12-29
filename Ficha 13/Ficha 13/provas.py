# Biblioteca Tkinter: UI
from tkinter import *
from tkinter import messagebox

fProvas= "files/provas.txt"


def inserirProva(prova, data, local, tipoProva, lstprovas):
    fileProvas=open(fProvas, "a", encoding="utf-8")
    linha = prova + ";" + data + ";" + local + ";" + tipoProva + "\n" 
    fileProvas.write(linha)
    fileProvas.close()
    
    lista = lerProvas()
    refreshListboxProvas(lista, lstprovas)
   

def lerProvas():
    fileProvas=open(fProvas, "r", encoding="utf-8")
    lista = fileProvas.readlines()
    fileProvas.close()
    return lista

def refreshListboxProvas(listaProvas, lstprovas):
    lstprovas.delete(0, END)
    for item in listaProvas:
        item = item.replace(";", " ")
        lstprovas.insert(END, item)