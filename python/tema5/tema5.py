import math

#CALCULA EL AREA DEL TRIANGULO
b = float(input("ingresa la base del triangulo: "))
a = float(input("ingresa la altura del triangulo: "))
a = b * a / 2
print("el area del triangulo es: ", a)


#CALCULA EL AREA DEL CIRCULO

r = float(input("ingresa el radio del circulo: "))
a = math.pi * (r * r)
print("el área del circulo es: ", round(a, 2))