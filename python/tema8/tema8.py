file = open('mi primer archivo desde python.txt', 'w')
file.write('estoy creando mi primer archivo desde python.\n')
file.close()

file = open('mi primer archivo desde python.txt', 'r+')
file.readline()
file.write('estoy escribiendo mas.\n')

file.seek(0)
print(file.read())
file.close()