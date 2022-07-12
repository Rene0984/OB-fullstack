from tkinter import *

master = Tk()

nombre = StringVar()

lista = Listbox(master)

for item in ['Perro', 'Gato', 'Caballo', 'Cerdo', 'Lobo', 'Serpiente', 'León', 'Tigre' ]:
    lista.insert(END, item)
lista.pack()
    
label = Label(text='Nombre de Animales')
label.pack()

master.mainloop()