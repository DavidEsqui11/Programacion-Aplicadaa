from email.mime import image
import this
from tkinter import*
from tkinter.font import BOLD
from turtle import heading
import Pruebas



def paginaregister():

    #Raiz
    ventana2=Tk()
    ventana2.title("Scrum")
    ventana2.resizable(False, False)
    ventana2.geometry("900x500")
    ventana2.iconbitmap("Scrum.ico")



    #Bordes verdes
    recverde=Frame(ventana2)
    recverde.pack(side="left")
    recverde.config(bg="#00A75E", width=90, height=500)

    recverde2=Frame(ventana2)
    recverde2.pack(side="right", anchor="n")
    recverde2.config(bg="#00A75E", width=810, height=80)



    #Datos usuario
    textoregistro=Label(ventana2, text = "REGISTRATE", font = ("Times New Roman", 20)).place(x = 445, y = 100)

    nombretexto=Label(ventana2, text = "Nombres: ", font = ("Times New Roman", 13)).place(x = 210, y = 180)
    nombrecuadro=Entry(ventana2, font = ("Times New Roman", 10), width = 40, bd = 0, bg="#D6D6D6").place(x = 210, y = 205)

    apellidotexto=Label(ventana2, text = "Apellidos: ", font = ("Times New Roman", 13)).place(x = 550, y = 180)
    apellidocuadro=Entry(ventana2, font = ("Times New Roman", 10), width = 40, bd = 0, bg="#D6D6D6").place(x = 550, y = 205)

    correotexto=Label(ventana2, text = "Correo: ", font = ("Times New Roman", 13)).place(x = 210, y = 245)
    correocuadro=Entry(ventana2, font = ("Times New Roman", 10), width = 40, bd = 0, bg="#D6D6D6").place(x = 210, y = 270)

    direcciontexto=Label(ventana2, text = "Dirección: ", font = ("Times New Roman", 13)).place(x = 550, y = 245)
    direccioncuadro=Entry(ventana2, font = ("Times New Roman", 10), width = 40, bd = 0, bg="#D6D6D6").place(x = 550, y = 270)

    contraseñatexto=Label(ventana2, text = "Contraseña: ", font = ("Times New Roman", 13)).place(x = 210, y = 310)
    contraseñacuadro=Entry(ventana2, font = ("Times New Roman", 10), width = 40, bd = 0, bg="#D6D6D6", show = "*").place(x = 210, y = 335)

    confirmarcontratexto=Label(ventana2, text = "Confirmar contraseña: ", font = ("Times New Roman", 13)).place(x = 550, y = 310)
    confirmarcontracuadro=Entry(ventana2, font = ("Times New Roman", 10), width = 40, bd = 0, bg="#D6D6D6", show = "*").place(x = 550, y = 335)



    #Check box aceptar terminos y conidiciones
    terminos=Checkbutton(ventana2, text="Aceptar terminos y condiciones", font = ("Times New Roman", 13), bd = 0).place(x = 390, y = 390)



    #Botones
    registrarboton=Button(ventana2, text = "REGISTRAR", font = ("Times New Roman", 13), bg = "#D6D6D6", bd = 0, width = 15).place(x = 440, y = 435)

    volver=Button(ventana2, text="Iniciar\nSesión", font = ("Times New Roman", 13, BOLD), bg = "#00A75E", bd = 0, width = 6, fg = "white").place(x = 12, y = 430)

    #ventana2.mainloop()

#paginaregister()
