class Alumno:
    def inicializar(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

    def imprimir(self):
        print("Nombre: ", self.nombre)
        print("Calificacion: ", self.calificacion)

    def resultado(self):
        if self.calificacion < 5:
            print("El alumno no aprobo")

        else:
            print("El alumno aprobo!!")   

alumno1 = Alumno()
alumno2 = Alumno()

alumno1.inicializar("juan",9)
alumno2.inicializar("pedro",4)

alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()
