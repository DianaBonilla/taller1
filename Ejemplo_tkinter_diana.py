## Ejemplo Aplicacion del tkinter.py
## Autor: Diana Bonilla
## Fecha: 18 - Diciembre - 2016

from tkinter import *

## funcion segunda ventana

def nuevo():
    v = Tk()
    v.title("Ejemplo \"tkinter\" Diana")
    v.configure(bg = 'coral')
    ## frame dentro de la ventana
    frame = Frame(v,relief = RIDGE,borderwidth=10)
    frame.grid(row = 0, column = 0)

    ## etiquetas
    et1 = Label(frame,
                text="Diana",
                font="Algerian 30",
                fg="purple",
                bg="DeepPink")

    et1.grid(row=0)

    et2 = Label(v,text="No hay nada en la vida que no contenga sus "
                "lecciones. Si estás vivo, siempre tendrás "
                "algo para aprender.\n",
                font="Calibri 14",
                fg="purple")

    et2.grid(row=1)
    ## botones
    boton = Button(v,text = "Salir",
                    font = "Calibri 15 bold",
                    fg="Moccasin",
                    bg="Magenta",
                    command = v.destroy)
    boton.grid(row=5,column = 1)
    
##    ## imagen
##    imagen = PhotoImage(file="frase.gif")
##    label1 = Label(v,image = imagen)
##    label1.grid(row=3, column=1)
##    v.mainloop()


    
## ventana principal
widget = Button(None,text='Siguiente',
                font = "Calibri 15 bold",
                fg = "DeepPink",
                bg = "Aqua",
                command = nuevo)
widget.grid(row = 3,column = 2)

## etiquetas
widget=Label(text="Ejemplo Tkinter",
             font = "Algerian 20",
             fg = "DarkBlue", ## color de fuente
             bg = "SkyBlue") ## color de fondo de la etiqueta 
widget.grid(row=0,column=1)


widget=Label(text="Construye tus sueños o alguien "
             "más te contratará para construir los suyos.",
             font = "Arial 14",
             fg = "Black") 
widget.grid(row=1,column=1)

## imagen
imagen1=PhotoImage(file="bien.gif")
widget = Label(image=imagen1)
widget.grid(row=2, column=1)

widget.mainloop()













