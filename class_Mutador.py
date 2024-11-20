
import os 
class Mutador():
    """
    Esta es la superclase mutador, contiene métodos que van
    a ser utilizados por las clases hijas

    Se considera mutar a que una matriz(AND)
    contenga un secuencia de más de 3 bases
    iguales
    """ # Cantidad de veces que se repite la base

    def __init__(self) -> None:# Metodo constructor
        self.cantidad = 4
        self.coordenadas = {# Coordendas para iterar en diagonal
    "fila:1" : [[3, 0], [2, 1], [1, 2], [0, 3]],
    "fila:2" : [[4, 0], [3, 1], [2, 2], [1, 3], [0, 4]],
    "fila:3" : [[5, 0], [4, 1], [3, 2], [2, 3], [1, 4], [0, 5]],
    "fila:4" : [[5, 1], [4, 2], [3, 3], [2, 4], [1, 5]],
    "fila:5" : [[5, 2], [4, 3], [3, 4], [2, 5]]
    }
        #self.adn = adn
        #self.base = base
        #self.direccion = direccion

    def crear_mutante(self) -> None:# Método polimorfico que crea mutaciones
        """
        Método polimorfico que crea mutaciones
        tambíen llama a otros metodos necesarios para mejorar la visualización
        """
        pass
        """self.separar()
        print("\nElija donde quiere generar el mutante")
        self.mostrar_coordenadas()
        self.separar()"""

    def mostrar_coordenadas(self) -> None:
        """
        Método que imprime una matriz con el fin de que el usuario
        pueda ver las coordenadas de todas las posiciones 
        """
        normal = [[f"F:{i} C:{j}| " for j in range(6)] for i in range(6)] # Se crea una matriz
        print("\nF: Fila | C: Columna") # Muestra al usuario como guiarse por la matriz
        self.separar()
        print("\n".join("  ".join(normal[i][j] for j in range(6)) for i in range(6)))# Imprime la matriz
    
    def separar(self) -> None:
        """
        Este método crea una línea para separar
        se creo para mas facilidad en el uso
        """
        print("---------------------------------------------------------------")
    
    def limpiar_consola(self) -> None:
        """
        Método que limpia la consola de ser necesario
        Su uso es cuando ya no es necesaria mostrar cierta información
        """
        if os.name == 'nt':  # Para Windows
            os.system('cls')
        else:  # Para sistemas Unix (Linux/macOS)
            os.system('clear')
