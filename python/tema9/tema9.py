class Vehiculo():
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.puertas = puertas
        self.ruedas = ruedas

    def __str__(self):
        return "Color {}, {} ruedas".format(self.color, self.puertas, self.ruedas )

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        self.color = color
        self.puertas = puertas
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return "color {}, {} kmh, {} ruedas, {} puertas, {} cc".format(
            self.color, self.velocidad, self.ruedas, self.puertas, self.cilindrada )

coche = Coche("blanco", 4, 2, 120, 1800)
print(coche)