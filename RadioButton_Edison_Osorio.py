print ('\t EDISON OSORIO\n')
from tkinter import *
def operacion():
    numero=num.get()
    if opcion.get()==1:
        total=numero*10
    elif opcion.get()==2:
        total=numero*20
    elif opcion.get()==3:
        total=numero*30
    elif opcion.get()==4:
        total=numero*40
    elif opcion.get()==5:
        total=numero*50
    else:
        total=numero*numero
    print('EL TOTAL DE LA OPERACIÖN ES: '+str(total))

ventana=Tk()
opcion=IntVar()
num=IntVar()
ventana.title('....EJERCICIO RADIOBUTTON....')
ventana.geometry('400x300')
etiqueta=Label(ventana,text='escribe un numero: ').place(x=20, y=20)
cajaNumero=Entry(ventana, textvariable=num).place(x=130, y=20)
cajaNumero=Label(ventana,text='Escribe tu opcion: ').place(x=20, y=50)
x10=Radiobutton(ventana,text='x10',value=1, variable=opcion).place(x=20, y=80)
x20=Radiobutton(ventana,text='x20',value=2, variable=opcion).place(x=70, y=80)
x30=Radiobutton(ventana,text='x30',value=3, variable=opcion).place(x=120, y=80)
x40=Radiobutton(ventana,text='x40',value=4, variable=opcion).place(x=20, y=110)
x50=Radiobutton(ventana,text='x50',value=5, variable=opcion).place(x=70, y=110)
cuadrado=Radiobutton(ventana, text='cuadrado', value=6, variable=opcion).place(x=120, y=110)
boton =Button (ventana, text='Realiza una operacion', command=operacion).place(x=20, y=40)
ventana.mainloop()
