lugar = input ("Escribe paises separados por comas: \n")

paises = [pais for pais in lugar.split(",")]

print(",".join(sorted(list(set(paises)))))