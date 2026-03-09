# Definir la clase Estudiante
class Estudiante:
    def __init__(self, nombre, edad, calificacion):
        # Constructor para inicializar el estudiante con nombre, edad y calificación
        self.nombre = nombre
        self.edad = edad
        self.calificacion = calificacion

    def es_aprobado(self):
        # Método para determinar si el estudiante aprobó o reprobó
        # Supongamos que la calificación mínima para aprobar es 6
        if self.calificacion >= 6:
            return f"{self.nombre} aprobó con calificación {self.calificacion}."
        else:
            return f"{self.nombre} reprobó con calificación {self.calificacion}."

# Crear un objeto Estudiante
est1 = Estudiante("Ana", 20, 7.5)
est2 = Estudiante("Luis", 19, 5.8)

# Mostrar resultado si aprobaron o reprobaron
print(est1.es_aprobado())
print(est2.es_aprobado())