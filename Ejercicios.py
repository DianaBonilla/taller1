from tkinter import *

print("\tEscuela Politecnica Nacional")
print("Integrantes: ")
print("Bonilla Diana")
print("Jessica Carrillo")
print("Edison Hernandez")
print("Edison Osorio")
print("Jordan Sanchez")

print("\nEjercicio 1")
root = Tk()
etiqueta1=Label(root, text="Hello Tkinter..!!")
etiqueta1.pack()
root.mainloop()

print("\nEjercicio 2")
master=Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it. \n(Mahatma Gandhi)"
msg=Message(master, text=whatever_you_do)
msg.config(bg='lightgreen', font=('times',24, 'italic'))
msg.pack()
mainloop()

print("\nEjercicio 3")
class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        self.button = Button(frame, text="SALIR",
    fg="red",command=frame.quit)
        self.button.pack(side=LEFT)
        self.slogan =Button(frame,text="ENTRAR",command=self.write_slogan)
        self.slogan.pack(side=LEFT)
    def write_slogan(self):
            print ("Estamos aprendiendo a usar Tkinter!")
            
print("\nEjercicio 4")
root = Tk()
app = App(root)
root.mainloop()

root = Tk()
v = IntVar()
Label(root,
      text="""Choose a programming language:""",
      justify = LEFT,
      padx = 20).pack()
Radiobutton(root,
            text="Python",
            padx = 20, variable=v,
            value=1).pack(anchor=W)
Radiobutton(root,
            text="Perl",
            padx = 20,
            variable=v,
            value=2).pack(anchor=W)
mainloop()

##Ejercicio 5
from tkinter import *
root = Tk()
v = IntVar()
v.set(1)  # initializing the choice, i.e. Python
print("Ejercicio 5")
languages = [("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)]
def ShowChoice():
    print (v.get())
Label(root, 
    text="""Choose your favourite programming language:""",
    justify = LEFT,
    padx = 20).pack()
for txt, val in languages:
    Radiobutton(root, 
    text=txt,
    padx = 30, 
    variable=v, 
    command=ShowChoice,
    value=val).pack(anchor=W)
mainloop()

##Ejercicio 6
from tkinter import *
root1 = Tk()
v = IntVar()
v.set(1)  # initializing the choice, i.e. Python
print("Ejercicio 6")
languages = [("Python",1),
    ("Perl",2),
    ("Java",3),
    ("C++",4),
    ("C",5)
    ]
def ShowChoice1():
    print (v.get())
Label(root1, 
    text="""Escoja un lenguaje de programación:""",
    justify = LEFT,
    padx = 20).pack()
for txt, val in languages:
    Radiobutton(root1, 
    text=txt,
    indicatoron =0,
    width = 20,
    padx = 20, 
    variable=v, 
    command=ShowChoice1,
    value=val).pack(anchor=W)


##EJERCICIO 7

from tkinter import *
master = Tk()
master.title('EJERCICIO 7')
print("Ejercicio 7")
Button(master,text="finalizar",command=master.quit).grid(row=2,column=2)
var1 = IntVar()
Checkbutton(master, text="Hombre", variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(master, text="Mujer", variable=var2).grid(row=1, sticky=W)
master.mainloop()


##EJERCICIO 8
from tkinter import*
master = Tk()
master.title('EJERCICIO 8')
print("Ejercicio 8")
def var_states():
    print (" hombre: ",var1.get())
    print ("mujer: ",var2.get())
Label(master, text="Indicar el sexo:").grid(row=0, sticky=W)
var1 = IntVar()
Checkbutton(master, text="Hombre", variable=var1).grid(row=1,sticky=W)
var2 = IntVar()
Checkbutton(master, text="Mujer", variable=var2).grid(row=2,sticky=W)
Button(master, text='Quit', command=master.quit).grid(row=3,sticky=W, padx=4)
Button(master, text='Show', command=var_states).grid(row=4,sticky=W, pady=4)
master.mainloop()

var_states()

#EJERCICIO #9

from tkinter import*
master=Tk()
master.title('EJERCICIO # 9')
Label(master, text='First Name').grid(row=0)
Label(master, text='Laste Name').grid(row=1)
e1=Entry(master)
e2=Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
mainloop()

#EJERCICIO #10

from tkinter import*
def show_entry_fields():
    print('First Name: %s\nLast Name: %s' %(e1.get(),e2.get()))

master =Tk()
master.title('EJERCICIO # 10')
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)

e1=Entry(master)
e2=Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit',command=master.quit).grid(row=3,column=0, sticky=W,pady=4)
Button(master,text='Show',command=show_entry_fields).grid(row=3 , column=1, sticky=W, pady=4)
master.mainloop()
