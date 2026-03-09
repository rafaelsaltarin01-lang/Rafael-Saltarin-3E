class Vehiculo:
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0  # velocidad inicial

    def acelerar(self, incremento):
        # Aumenta la velocidad sin superar la velocidad máxima
        nueva_velocidad = self.velocidad_actual + incremento
        if nueva_velocidad > self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_maxima
        else:
            self.velocidad_actual = nueva_velocidad
        print(f"Velocidad actual: {self.velocidad_actual} km/h")

    def frenar(self, decremento):
        # Reduce la velocidad sin bajar de 0
        nueva_velocidad = self.velocidad_actual - decremento
        if nueva_velocidad < 0:
            self.velocidad_actual = 0
        else:
            self.velocidad_actual = nueva_velocidad
        print(f"Velocidad actual: {self.velocidad_actual} km/h")

    def verificar_limite(self, velocidad_limite):
        # Verifica si la velocidad actual supera el límite dado
        if self.velocidad_actual > velocidad_limite:
            print(f"¡Alerta! La velocidad actual ({self.velocidad_actual} km/h) supera el límite de {velocidad_limite} km/h.")
        else:
            print(f"La velocidad actual ({self.velocidad_actual} km/h) está dentro del límite de {velocidad_limite} km/h.")


# Programa principal con menú
def menu():
    print("Bienvenido al sistema de monitoreo de velocidad")
    marca = input("Ingrese la marca del vehículo: ")
    modelo = input("Ingrese el modelo del vehículo: ")
    while True:
        try:
            velocidad_maxima = float(input("Ingrese la velocidad máxima del vehículo (km/h): "))
            if velocidad_maxima <= 0:
                print("La velocidad máxima debe ser un número positivo.")
                continue
            break
        except ValueError:
            print("Por favor, ingrese un número válido para la velocidad máxima.")

    vehiculo = Vehiculo(marca, modelo, velocidad_maxima)

    while True:
        print("\nMenú:")
        print("1. Acelerar")
        print("2. Frenar")
        print("3. Verificar si excede un límite de velocidad")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            try:
                incremento = float(input("Ingrese cuánto desea acelerar (km/h): "))
                if incremento < 0:
                    print("El incremento debe ser positivo.")
                    continue
                vehiculo.acelerar(incremento)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == "2":
            try:
                decremento = float(input("Ingrese cuánto desea frenar (km/h): "))
                if decremento < 0:
                    print("El decremento debe ser positivo.")
                    continue
                vehiculo.frenar(decremento)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == "3":
            try:
                limite = float(input("Ingrese el límite de velocidad a verificar (km/h): "))
                if limite < 0:
                    print("El límite debe ser un número positivo.")
                    continue
                vehiculo.verificar_limite(limite)
            except ValueError:
                print("Por favor, ingrese un número válido.")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el menú
menu()