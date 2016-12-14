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

