from tkinter import *


def seleccionar():
    monitor.config(text="{}".format(opcion.get()))

def reiniciar():
    opcion.set(None)
    monitor.config(text="")
    
root = Tk()
opcion = StringVar()
opcion.set(None)

Radiobutton(root, text="Chevrolet", variable=opcion, value='Chevrolet', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Ford", variable=opcion, value='Ford', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Dodge", variable=opcion, value='Dodge', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Volkswagen", variable=opcion, value='Volkswagen', command=seleccionar).pack(anchor=W)

monitor = Label(root)
monitor.pack()
Button(root, text="Reiniciar", command=reiniciar).pack()

root.mainloop()