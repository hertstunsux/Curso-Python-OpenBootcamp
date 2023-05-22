class Alumno:
    def __init__ (self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
    def __str__(self):
        return "El alumno {} ha aprobado con nota {}".format(self.nombre,self.nota) if self.nota>50 else "El alumno {} ha reprobado con nota {}".format(self.nombre,self.nota)


Sebastian = Alumno("Sebastian", 30)
print(Sebastian)