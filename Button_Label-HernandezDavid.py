from tkinter import *
print("David Hernandez")

def despedida():
    lblSaludar=Label(ventana,text="Adios "+ entradaN.get(),font=("Agency FB",14)).place(x=10,y=140)
def saludar():
    lblSaludar=Label(ventana,text="Hola "+ entradaU.get(),font=("Agency FB",14)).place(x=10,y=110)
ventana= Tk()
ventana.geometry("500x300+100+100")
ventana.title("David Hernandez, Ejercicio Taller 1")
lblUsuario=Label(text="Usuario: ",font=("Agency FB",14)).place(x=10,y=10)
#Crear campos de texto
entradaU=StringVar()
txtUsuario= Entry(ventana,textvariable=entradaU).place(x=70,y=20)
entradaN=StringVar()
lblNombre=Label(text="Nombre: ",font=("Agency FB",14)).place(x=10,y=50)
txtNombre= Entry(ventana,textvariable=entradaN, width=30).place(x=70,y=60)
#Crear botones 
btnDave=Button(ventana,text="Saludar",command= saludar,font=("Agency FB",14),width=10).place(x=300,y=20)
btnEd=Button(ventana,text="Despedir",command=despedida,font=("Agency FB",14),width=10).place(x=300,y=70)
ventana.mainloop()
