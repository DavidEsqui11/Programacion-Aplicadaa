import imp
from tkinter import*
from tkinter.font import BOLD
from turtle import heading



def paginatodo():

    #Raiz
    ventana4=Tk()
    ventana4.title("Scrum")
    ventana4.resizable(False, False)
    ventana4.geometry("900x500")
    ventana4.iconbitmap("Scrum.ico")



    #Bordes verdes
    recverde=Frame()
    recverde.pack(side="left")
    recverde.config(bg="#00A75E", width=90, height=500)

    recverde2=Frame()
    recverde2.pack(side="right", anchor="n")
    recverde2.config(bg="#00A75E", width=810, height=80)



    #Boton de cerrar sesión
    volver=Button(ventana4, text="Cerrar\nSesión", font = ("Times New Roman", 13, BOLD), bg = "#00A75E", bd = 0, width = 6, fg = "black").place(x = 12, y = 430)



    #Botones
    volverproyectos=Button(ventana4, text="Volver a\nProyectos", font = ("Times New Roman", 13, BOLD), bg = "#00A75E", bd = 0, width = 7, fg = "black").place(x = 6, y = 80)
    volverinprogress=Button(ventana4, text="Volver a\nIn Progress", font = ("Times New Roman", 12, BOLD), bg = "#00A75E", bd = 0, width = 8, fg = "black").place(x = 6, y = 150)
    volverdone=Button(ventana4, text="Volver a\nDone", font = ("Times New Roman", 13, BOLD), bg = "#00A75E", bd = 0, width = 7, fg = "black").place(x = 6, y = 220)



    #Textos
    textotodo=Label(ventana4, text = "To Do", font = ("Times New Roman", 20, BOLD)).place(x = 465, y = 100)

    


    ventana4.mainloop()


paginatodo()