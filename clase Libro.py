# Definir la clase Libro
class Libro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def mostrar_informacion(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Número de páginas: {self.num_paginas}")

    def actualizar_paginas(self, nuevo_num_paginas):
        self.num_paginas = nuevo_num_paginas
        print(f"Número de páginas actualizado a: {self.num_paginas}")


mi_libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 417)


mi_libro.mostrar_informacion()


mi_libro.actualizar_paginas(420)


mi_libro.mostrar_informacion()
