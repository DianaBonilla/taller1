#Ejemplo de aplicacion de Tkinter
#Jordan Sanchez

from tkinter import *

def hacer_click():
    try:
        valorUno = int(valor1.get())
        valorDos = int(valor2.get())
        Suma = valorUno + valorDos
        etiqueta1.config(text="Suma: "+ str(Suma))
        Resta = valorUno - valorDos
        etiqueta2.config(text="Resta: "+ str(Resta))
        Multi = valorUno * valorDos
        etiqueta3.config(text="Multiplicacion: "+ str(Multi))
        if valorDos == 0:
            etiqueta4.config(text="No hay Division para 0")
        else:    
            Div = valorUno / valorDos
            etiqueta4.config(text="Division: "+ str(Div))
    except ValueError:
        etiqueta.config(text="Introduce un numero!")
 
 
calculadora = Tk()
calculadora.title("Ejemplo Jordan Sanchez")
 
vp = Frame(calculadora)
vp.grid(column=0, row=0, padx=(50,80), pady=(10,10))
vp.columnconfigure(0, weight=1)
vp.rowconfigure(0, weight=1)
 
etiqueta1 = Label(vp, text="Suma: ")
etiqueta1.grid(column=2, row=2, sticky=(W,E))
etiqueta2 = Label(vp, text="Resta: ")
etiqueta2.grid(column=2, row=4, sticky=(W,E))
etiqueta3 = Label(vp, text="Multiplicacion: ")
etiqueta3.grid(column=2, row=6, sticky=(W,E))
etiqueta4 = Label(vp, text="Division: ")
etiqueta4.grid(column=2, row=8, sticky=(W,E))
 
boton = Button(vp, text="Calcular", command=hacer_click)
boton.grid(column=1, row=1)
 
valor = ""
valor1 = Entry(vp, width=5, textvariable=valor)
valor1.grid(column=2, row=1)
valor2 = Entry(vp, width=5, textvariable=valor)
valor2.grid(column=3, row=1)
 
calculadora.mainloop()
