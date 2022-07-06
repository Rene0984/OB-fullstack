from paquete.operaciones import *

a, b, c, d, = (25, 17, 9,11)

print("{} + {} = {}".format(a, b, suma(a,d)))
print("{} - {} = {}".format(a, b, resta(b,c)))
print("{} * {} = {}".format(a, b, multiplicacion(c,d)))
print("{} / {} = {}".format(a, b, division(a,b)))