import os 
import random

class Detector:
    # Clase para detectar secuencias mutantes en una matriz de ADN.
    
    # Constantes para la detección de mutantes
    CANTIDAD_MAXIMA = 3  # Máximo de bases iguales consecutivas permitidas
    rango_secuencia = 6  # Tamaño de las secuencias en la matriz (6x6)
    coordenadas = {  # Coordenadas para detectar secuencias diagonales
        "d1": [(3, 0), (2, 1), (1, 2), (0, 3)],
        "d2": [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)],
        "d3": [(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)],
        "d4": [(5, 1), (4, 2), (3, 3), (2, 4), (1, 5)],
        "d5": [(5, 2), (4, 3), (3, 4), (2, 5)]
    }

    def __init__(self, adn: list) -> None:
        # Inicializa la matriz de ADN y un contador para bases consecutivas.
        self.adn = adn
        self.contador = 1

    def detectar_mutantes(self) -> bool:
        # Método principal que verifica si existen mutaciones.
        return self.mutantes()

    def mutantes(self) -> bool:
        # Verifica secuencias mutantes en todas las direcciones: horizontal, vertical y diagonal.
        return any(self.direcciones(direccion) for direccion in ["horizontal", "vertical", "diagonal", "diagonal.invertida"])

    def verficacion(self, lista: list, rango: int) -> bool:
        # Verifica si una lista contiene más de 3 bases iguales consecutivas.
        self.identidad = lista
        for j in range(1, rango):
            if self.identidad[j] == self.identidad[j-1]:
                self.contador += 1  # Incrementa el contador si las bases consecutivas son iguales.
            else:
                self.contador = 1  # Reinicia el contador si no son iguales.
            if self.contador > self.CANTIDAD_MAXIMA:
                return True
        return False

    def direcciones(self, direccion: str) -> bool:
        # Genera listas de secuencias según la dirección especificada y las verifica.
        if direccion == "horizontal":
            secuencias = [self.adn[fila] for fila in range(self.rango_secuencia)]
        elif direccion == "vertical":
            secuencias = [[self.adn[fila][columna] for fila in range(self.rango_secuencia)] for columna in range(self.rango_secuencia)]
        elif direccion == "diagonal":
            secuencias = self.diagonales(1)
        elif direccion == "diagonal.invertida":
            secuencias = self.diagonales(2)
        return any(self.verficacion(secuencia, len(secuencia)) for secuencia in secuencias)

    def diagonales(self, control: int) -> list:
        # Genera listas con las diagonales de la matriz (ascendentes y descendentes).
        if control == 1:
            return [[self.adn[x][y] for x, y in coords] for coords in self.coordenadas.values()]
        else:
            matriz_invertida = [list(reversed(fila)) for fila in self.adn]
            return [[matriz_invertida[x][y] for x, y in coords] for coords in self.coordenadas.values()]

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

class Viruz(Mutador):
    # Subclase que muta la matriz en sentido diagonal (ascendente o descendente).
    def __init__(self) -> None:# Inicializa el método contructor de la superclase
        super().__init__()
    
    def revertir(self,matriz: list) -> list:
        #Método que retorna una versión revertida de las sublistas de la matriz
        return [list(reversed(sublista)) for sublista in matriz]

    def mostrar_coordenadas(self,sentido) -> None:
        self.sentido = sentido
        matriz = [
            ["------", "------", "------", "Fila:1", "Fila:2", "Fila:3"],
            ["------", "------", "Fila:1", "Fila:2", "Fila:3", "Fila:4"],
            ["------", "Fila:1", "Fila:2", "Fila:3", "Fila:4", "Fila:5"],
            ["Fila:1", "Fila:2", "Fila:3", "Fila:4", "Fila:5", "------"],
            ["Fila:2", "Fila:3", "Fila:4", "Fila:5", "------", "------"],
            ["Fila:3", "Fila:4", "Fila:5", "------", "------", "------"]
        ]
        if self.sentido == 1:# Sentido ascente
            print("\n".join("  ".join(matriz[i][j] for j in range(6)) for i in range(6)))
        else:
            # Sentido descendente
            matriz = self.revertir(matriz) # Se revierte la matriz
            print("\n".join("  ".join(matriz[i][j] for j in range(6)) for i in range(6)))

    def fila(self):
        while True:# Se verifica que el usuario ingrese de forma correta el input
            fila  = input("\nIngrese el número de la fila seleccionada: ")
            # Se verfica que la entrada corresponda a las claves del diccionario de coordenadas
            if fila in self.coordenadas.keys() and len(fila) == 1 :
                break
            else:
                print("Opción invalida")
        if self.sentido == 1: # Ascendente
            print(f"Has seleccionado la {fila}º. Coordenadas: {self.coordenadas[fila]}")
            self.secuencia = self.coordenadas[fila]
        else:
            # Descendente
            coordenadas = list(reversed(self.coordenadas[fila])) # Revierte la lista de coordenadas
            print(f"Has seleccionado la {fila}. Coordenadas: {coordenadas}")
            self.secuencia = coordenadas

    def crear_mutante(self, adn: list, base: str, origen: int) -> list:
        # Realiza una mutación en sentido diagonal.
        control = False
        while True:
            try:
                if control == True:
                    origen = input("Ingrese la coordenada inicial (Fila, Columna. Ej: 21): ")
                if len(origen) != 2 :
                    raise ValueError("Formato inválido.")
                origen = list(map(int, origen))
                inicio = self.secuencia.index(origen)# Se guarda el indice perteneciente al origen introducido
                # secuencia = self.coordenadas["fila:1"]  # Ejemplo para simplificar lógica
                for i in range(self.cantidad):
                    fila, columna = self.secuencia[inicio + i]
                    adn[fila][columna] = base
                print("\nMutante creado.")
                return adn
            except ValueError as error:
                self.limpiar_consola()
                print(f"\nError: {error}. Intente nuevamente.")
                control = True
                sentido = self.sentido # Esto es muy importante, es redundante pero con esto se asegura que las coordenadas sean las correctas
                self.mostrar_coordenadas()
                print(self.secuencia)
            except IndexError:
                self.limpiar_consola()
                print("\nError: Fuera de rango de la matriz | RECUERDE: la base se repite 4 veces dentro del rango de la fila")
                control = True
                sentido = self.sentido # Esto es muy importante, es redundante pero con esto se asegura que las coordenadas sean las correctas
                self.mostrar_coordenadas(sentido)
                print(self.secuencia)