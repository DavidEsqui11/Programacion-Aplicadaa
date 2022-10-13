from cProfile import label
from distutils.command.config import config
from email.mime import image
import imp
from tkinter import*
from tkinter.font import BOLD
from turtle import heading



def paginasproyectos():
    #Raiz
    ventana=Tk()
    ventana.title("Scrum")
    ventana.resizable(False, False)
    ventana.geometry("900x500")
    ventana.iconbitmap("Scrum.ico")



    #Bordes verdes
    recverde=Frame()
    recverde.pack(side="left")
    recverde.config(bg="#00A75E", width=90, height=500)

    recverde2=Frame()
    recverde2.pack(side="right", anchor="n")
    recverde2.config(bg="#00A75E", width=810, height=80)

    textoregistro=Label(ventana, text = "PROYECTOS", font = ("Times New Roman", 20, BOLD)).place(x = 425, y = 100)



    #Cuadro ver proyectos
    imagencrear = PhotoImage(file="crear.png")
    crearimg = Button(ventana, image = imagencrear).place(x = 575, y = 225)

    imagenproyectos = PhotoImage(file="proyectos.png")
    proyectosimg = Button(ventana, image = imagenproyectos).place(x = 215, y = 225)



    #Botones crear y ver proyectos
    proyectostexto=Label(ventana, text = "Ver Proyectos", font = ("Times New Roman", 13), bd = 0, width = 15).place(x = 256, y = 335)

    creartexto=Label(ventana, text = "Crear Proyecto", font = ("Times New Roman", 13), bd = 0, width = 15).place(x = 617, y = 335)



    #Boton de cerrar sesión
    volver=Button(ventana, text="Cerrar\nSesión", font = ("Times New Roman", 13, BOLD), bg = "#00A75E", bd = 0, width = 6, fg = "black").place(x = 12, y = 430)

    ventana.mainloop()

paginasproyectos()