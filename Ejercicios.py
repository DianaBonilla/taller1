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
