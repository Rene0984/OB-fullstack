from functools import reduce

def mifuncion(lista):
    resultado = list(filter((lambda x: x % 2), lista))
    print(resultado)
    resultado = reduce( (lambda x, y: x + y), resultado)
    print(resultado)
    
lista = list(range(100))

mifuncion(lista)