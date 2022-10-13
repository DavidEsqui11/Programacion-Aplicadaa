import imp
from tkinter import*
from tkinter.font import BOLD
from turtle import heading



def paginamenus():

    #Raiz
    ventana3=Tk()
    ventana3.title("Scrum")
    ventana3.resizable(False, False)
    ventana3.geometry("900x500")
    ventana3.iconbitmap("Scrum.ico")



    #Bordes verdes
    recverde=Frame()
    recverde.pack(side="left")
    recverde.config(bg="#00A75E", width=90, height=500)

    recverde2=Frame()
    recverde2.pack(side="right", anchor="n")
    recverde2.config(bg="#00A75E", width=810, height=80)



    #Boton de cerrar sesión
    volver=Button(ventana3, text="Cerrar\nSesión", font = ("Times New Roman", 13, BOLD), bg = "#00A75E", bd = 0, width = 6, fg = "black").place(x = 12, y = 430)



    #Botones
    imagenprogress = PhotoImage(file="inprogress2.png")
    crearimg = Button(ventana3, image = imagenprogress, bg="white", bd = 1).place(x = 420, y = 200)

    imagendone = PhotoImage(file="done2.png")
    crearimg = Button(ventana3, image = imagendone, bg="white", bd = 1).place(x = 630, y = 200)

    imagentodo = PhotoImage(file="to-do.png")
    crearimg = Button(ventana3, image = imagentodo, bg="white", bd = 1).place(x = 210, y = 200)

    volverproyectos=Button(ventana3, text="Volver a\nProyectos", font = ("Times New Roman", 13, BOLD), bg = "#00A75E", bd = 0, width = 7, fg = "black").place(x = 6, y = 230)



    #Textos
    textotodo=Label(ventana3, text = "To Do", font = ("Times New Roman", 13)).place(x = 257, y = 352)
    textoinprogress=Label(ventana3, text = "In Progress", font = ("Times New Roman", 13)).place(x = 452, y = 352)
    textodone=Label(ventana3, text = "Done", font = ("Times New Roman", 13)).place(x = 676, y = 352)
    textomenu=Label(ventana3, text = "MENÚ", font = ("Times New Roman", 20, BOLD)).place(x = 460, y = 100)
    


    ventana3.mainloop()


paginamenus()