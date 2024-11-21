class Radiacion(Mutador):
    # Subclase que muta la matriz en sentido horizontal o vertical.
    def __init__(self) -> None:# Inicializa el método contructor de la superclase
        super().__init__()

    def crear_mutante(self, adn: list, direccion: int, base: str, origen: int) -> list:
        # Realiza una mutación en sentido horizontal o vertical.
        control = False
        while True:
            try:
                if control == True:
                    origen = input("Ingrese la coordenada inicial (Fila, Columna. Ej: 21): ")
                if len(origen) != 2:
                    raise ValueError("Formato inválido.")
                fila, columna = map(int, origen)
                
                indices = [(fila, columna + i) for i in range(self.cantidad)] if direccion == 1 else [(fila + i, columna) for i in range(self.cantidad)]
                
                for x, y in indices:
                    adn[x][y] = base
                print("\nMutante creado.")
                return adn
            except ValueError as error:
                self.limpiar_consola()
                print(f"\nError: {error}. Intente nuevamente.")
                control = True
                self.mostrar_coordenadas()
            except IndexError:
                self.limpiar_consola()
                print("\nError: Fuera de rango de la matriz | RECUERDE: la base se repite 4 veces dentro del rango de la fila")
                control = True
                self.mostrar_coordenadas()
