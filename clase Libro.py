# Definir la clase Libro
class Libro:
    def __init__(self, titulo, autor, num_paginas):
        # Constructor para inicializar los atributos del libro
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def mostrar_informacion(self):
        # Método para mostrar la información del libro
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.num_paginas}")

    def actualizar_paginas(self, nuevo_num_paginas):
        # Método para actualizar el número de páginas del libro
        self.num_paginas = nuevo_num_paginas
        print(f"Número de páginas actualizado a: {self.num_paginas}")

# Crear un objeto Libro
mi_libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 417)

# Mostrar información original del libro
mi_libro.mostrar_informacion()

# Actualizar el número de páginas
mi_libro.actualizar_paginas(420)

# Mostrar la información actualizada
mi_libro.mostrar_informacion()