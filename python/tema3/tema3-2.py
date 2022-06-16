peso = input ("cual es tu peso en kg?")
estatura = input ("cual es tu estatura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("tu imc es " + str(imc))
