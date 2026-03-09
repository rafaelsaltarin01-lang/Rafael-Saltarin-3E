# Definir la clase Producto
class Producto:
    def __init__(self, nombre, precio, stock):
        # Inicializa el producto con nombre, precio y cantidad en stock
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def verificar_disponibilidad(self, cantidad):
        # Verifica si hay suficiente stock para la cantidad solicitada
        if cantidad <= self.stock:
            return True
        else:
            return False

    def vender(self, cantidad):
        # Intenta vender una cantidad de producto si hay stock suficiente
        if self.verificar_disponibilidad(cantidad):
            self.stock -= cantidad
            print(f"Se vendieron {cantidad} unidades de {self.nombre}. Stock restante: {self.stock}")
        else:
            print(f"No hay suficiente stock para vender {cantidad} unidades de {self.nombre}.")

    def reabastecer(self, cantidad):
        # Añade más cantidad al stock disponible
        self.stock += cantidad
        print(f"Se reabastecieron {cantidad} unidades de {self.nombre}. Nuevo stock: {self.stock}")

# Crear el objeto Producto con los valores iniciales
producto = Producto("Laptop", 1200, 10)

# Operaciones solicitadas

# 1. Verificar si hay 5 unidades disponibles
print("¿Hay 5 unidades disponibles?", producto.verificar_disponibilidad(5))

# 2. Vender 3 unidades
producto.vender(3)

# 3. Verificar si hay 8 unidades disponibles
print("¿Hay 8 unidades disponibles?", producto.verificar_disponibilidad(8))

# 4. Intentar vender 8 unidades (debe fallar)
producto.vender(8)

# 5. Reabastecer con 10 unidades adicionales
producto.reabastecer(10)

# 6. Verificar nuevamente si hay 8 unidades disponibles
print("¿Hay 8 unidades disponibles?", producto.verificar_disponibilidad(8))

# 7. Vender 8 unidades
producto.vender(8)