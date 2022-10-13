from cProfile import label
from distutils.command.config import config
from email.mime import image
import imp
import this
from tkinter import*
from tkinter.font import BOLD
from turtle import heading
#import pagregister



def paginalogin():
    #Raiz
    ventana=Tk()
    ventana.title("Scrum")
    ventana.resizable(False, False)
    ventana.geometry("900x500")
    ventana.iconbitmap("Scrum.ico")



    #Frame verde
    cuadroverde = Frame()
    cuadroverde.place(x = 510, y = 70)
    cuadroverde.config(bg = "#00A75E", width = 350, height = 350)

    textoiniciosesion=Label(ventana, text = "INICIA SESIÓN", font = ("Times New Roman", 20), bg = "#00A75E").place(x = 603, y = 100)



    #Usuario y contraseña
    usuariotexto=Label(ventana, text = "Usuario: ", font = ("Times New Roman", 13), bg = "#00A75E").place(x = 540, y = 160)
    usuariocuadro=Entry(ventana, font = ("Times New Roman", 10), width = 48, bd = 0).place(x = 540, y = 185)

    clavetexto=Label(ventana, text = "Contraseña: ", font = ("Times New Roman", 13), bg = "#00A75E").place(x = 540, y = 230)
    clavecuadro=Entry(ventana, font = ("Times New Roman", 10,), width = 48, show = "*", bd = 0).place(x = 540, y = 255)



    #Bontones
    botoniniciar=Button(ventana, text = "ENTRAR", font = ("Times New Roman", 13), bg = "white", bd = 0, width = 15).place(x = 620, y = 315)

    botonregistrar=Button(ventana, text = "Si no tienes cuenta, dale click aquí", font = ("Times New Roman", 11, BOLD), bg = "#00A75E", fg = "black", bd = 0).place(x = 567, y = 355)



    #Decoración
    textopublicidad=Label(ventana, text = "Nosotros te facilitamos la implementación de SCRUM", font = ("Times New Roman", 14)).place(x = 50, y = 310)

    imagenscrum = PhotoImage(file="5.png")
    fondo = Label(ventana, image = imagenscrum).place(x = 50, y = 80)
    ventana.mainloop()


paginalogin()