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
                self.mostrar_coordenadas()
            except IndexError:
                self.limpiar_consola()
                print("\nError: Fuera de rango de la matriz | RECUERDE: la base se repite 4 veces dentro del rango de la fila")
                control = True
                sentido = self.sentido # Esto es muy importante, es redundante pero con esto se asegura que las coordenadas sean las correctas
                self.mostrar_coordenadas(sentido)
                print(self.secuencia)