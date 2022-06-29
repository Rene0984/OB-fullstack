# solicita al usuario ingresar 2 numeros e imprime por consola los numeros impares entre los 2 numeros ingresados
# Ejemplo num_inicial= 2   num_funal= 8   imprimira= 3, 5, 7,


num_inicial= int(input("Hola!! introduce el primer numero: "))
num_final= int(input("introduce el numero final: "))

while num_inicial <= num_final:
   if num_inicial % 2:
       print(num_inicial)
   num_inicial += 1