class Mutador:
    # Clase base para mutar la matriz de ADN, utilizada por subclases.

    def __init__(self) -> None:
        self.cantidad = 4  # Número de bases consecutivas para una mutación
        self.coordenadas = {  # Coordenadas diagonales
            "1": [[3, 0], [2, 1], [1, 2], [0, 3]],
            "2": [[4, 0], [3, 1], [2, 2], [1, 3], [0, 4]],
            "3": [[5, 0], [4, 1], [3, 2], [2, 3], [1, 4], [0, 5]],
            "4": [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5]],
            "5": [[5, 2], [4, 3], [3, 4], [2, 5]]
        }

    def crear_mutantes(self):
        pass

    def mostrar_coordenadas(self) -> None:
        """
        Método que imprime una matriz con el fin de que el usuario
        pueda ver las coordenadas de todas las posiciones 
        """
        guia = [[f"F:{i} C:{j}| " for j in range(6)] for i in range(6)] # Se crea una matriz
        print("\nF: Fila | C: Columna") # Muestra al usuario como guiarse por la matriz
        print("\n".join("  ".join(guia[i][j] for j in range(6)) for i in range(6)))# Imprime la matriz

    def limpiar_consola(self) -> None:
        # Limpia la consola según el sistema operativo.
        os.system('cls' if os.name == 'nt' else 'clear')

