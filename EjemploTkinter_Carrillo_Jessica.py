from tkinter import*
   
def triangulo():
    try:
        _valor=int(entrada_texto.get())
        _valor2=int(entrada_texto2.get())
        _valor=(_valor*_valor2/2)
        etiqueta.config(text=_valor)
        etiqueta2.config(text=_valor2)
    except ValueError:
        etiqueta.config(text="Ingresar base y altura: ")

 
def Cuadrado():
    try:
        _valor=int(entrada_texto.get())
        _valor=(_valor*_valor)

        etiqueta.config(text=_valor)
    except ValueError:
        etiqueta.config(text="Ingresar lado: ")
   
def Circulo():
    try:
        _valor=int(entrada_texto.get())
        pi=3.1416
        _valor=(_valor**2*pi)
        etiqueta.config(text=_valor)
    except ValueError:
        etiqueta.config(text="Ingresar radio: ")
    
figu=Tk()
figu.title("CALCULO FIGURAS GEOMETRICAS")
vp=Frame(figu)
vp.grid(column=0, row=0, padx=(10,30), pady=(5,5))
vp.config(bg="black")
figu.geometry("600x500+0+0")
figu.config(bg="black")
imagenL=PhotoImage(file="figuras.png")
lblImagen=Label(figu,image=imagenL).place(x=50,y=105)
etiqueta=Label(vp, text="valor")
etiqueta.grid(column=0, row=3, sticky=(W,E))
etiqueta2=Label(vp, text="resultado de area")
etiqueta2.grid(column=0, row=4, sticky=(W,E))
etiqueta3=Label(vp,text="FIGURAS GEOMETRICAS\n",fg="white",font=("times",18),bg="black")
etiqueta3.grid(column=1, row=15,sticky=(W,E))
boton=Button(vp,text="CALCULO TRIANGULO",command=triangulo,bg="red")
boton.grid(column=0,row=1)
boton2=Button(vp,text="CALCULO CIRCULO",command=Circulo,bg="yellow")
boton2.grid(column=1,row=1)
boton3=Button(vp,text="CALCULO CUADRADO",command=Cuadrado,bg="lightblue")
boton3.grid(column=2,row=1)
boton4=Button(vp,text="SALIR CALCULO",command=figu.quit)
boton4.grid(column=2,row=3)

valor= ""
entrada_texto=Entry(vp, width=20, textvariable=valor)
entrada_texto.grid(column=1, row=3)
valor2= ""
entrada_texto2=Entry(vp, width=20, textvariable=valor2)
entrada_texto2.grid(column=1, row=4)

figu.mainloop()





        

