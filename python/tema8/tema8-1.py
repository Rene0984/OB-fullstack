from calendar import c
from pickle import *
import re
from this import d
from tkinter import N

class Vehiculo:
    def __init__(self, color, puertas):
        self.color = color
        self.puertas = puertas
        
    def __str__(self):
        return self.color + ' ' + self.puertas
    
cruze = Vehiculo("blanco", "4")
print("cruze")

file=open('vehiculo_objeto', 'w+b')

dump(cruze, file)

file.seek(0)
nuevo_cruze = load(file)

print(nuevo_cruze)
file.close()