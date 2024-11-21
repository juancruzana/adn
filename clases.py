import os 
import random

class Sanador(Detector):
    """
    Esta la Clase sanador, hereda métodos de la Clase Detector

    """
    __BASES_NITROGENADAS = ["A","C","G","T"] # Lista de las bases que contiene la matriz
    def __init__(self,adn: list) -> None:
        super().__init__(adn) # Inicializa el método constructor de la superclase

    def sanar_mutantes(self) -> list:
        """
        En este metodo se genera una matriz nueva
        si el método heredado (detectar_mutantes) retorna verdadero
        Caso contrario retorna la matriz introducida
        """
        if self.detectar_mutantes() == True:
            print("\nLa secuencia de ADN contiene mutaciones, comienza la curación")
            while True:
                """
                Mientras la nueva matriz contenga mutaciones, se generara otra matriz
                """
                # Se genera una nueva matriz con las bases selecionadas aleatoriamente
                self.adn = [[random.choice(self.__BASES_NITROGENADAS) for i in range(self.rango_secuencia)] for i in range(self.rango_secuencia)]
                if self.detectar_mutantes() == False: # Se verifica que la nueva matriz no contenga mutantes 
                    print("\nSecuencia curada con exito")
                    return self.adn
        else:
            print("\nLa secuencia de ADN no contiene mutaciones")
            return self.adn


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