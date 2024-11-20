from class_Mutador import * 

class Radiacion(Mutador):
    """
    Subclase encargada de mutar el ADN
    Solo muta en Horizontal y Vertical
    """
    def __init__(self) -> None:# Inicializa el método contructor de la superclase
        super().__init__()

    def crear_mutante(self,adn: list,base: str,direccion: int) -> list:
        self.adn = adn
        self.base = base
        self.direccion = direccion
        """
        Método heredado modificado
        Mientras se respete el fomato este método retorna una matriz modificada
        en caso contrario se le pedira al usuario que lo intente de nuevo
        """
        while True:
            try:
                print("\nElija donde quiere generar el mutante")
                print("\nMutante Horizontal") if self.direccion == 1 else print("\nMutante Vertical") # Muestra la dirección del usuario
                self.mostrar_coordenadas()
                # Pedir las coordenadas desde donde se inicia la mutación
                origen = input("\nIngrese la coordenada (Fila, Columna| Formato Ejemplo: 21): ")
                if len(origen) != 2:# Se crea una instancia de error si se la entrada es diferente al formato
                    raise ValueError("Ingrese solamente dos números seguidos: xy")
                fila, columna = map(int, origen)# Descompongo la lista en dos variables
                
                # Determinar los desplazamientos según la dirección
                if self.direccion == 1:  # Horizontal
                    indices = [(fila, columna + i) for i in range(self.cantidad)]
                else:  # Vertical
                    indices = [(fila + i, columna) for i in range(self.cantidad)]
                
                # Cambia los valores de las coordenadas de la matriz por la base ingresada por el usuario
                for x, y in indices:
                    self.adn[x][y] = self.base
                
                # Se retorna la matriz modificada
                print("\nMutante creado")
                return self.adn
            
            # Razones para pedir al usuario que lo intente devuelta
            except ValueError as error:# Ingresar mal los datos
                self.limpiar_consola()
                self.separar()
                print(f"\nError. {error}")
            except IndexError:# Ingresar un origen que produzca iterar fuera de la matriz
                self.limpiar_consola()
                self.separar()
                print("\nError: Fuera de rango de la matriz, la base se repite 4 veces dentro de un rango 0 a 5")

class Viruz(Mutador):
    """
    Subclase encargada de mutar el ADN en diagonal
    Muta en sentido Ascendente y Descendente
    """

    def __init__(self) -> None: # Inicializa el método constructor de la superclase
        super().__init__()

    def mostrar_coordenadas(self) -> None:
        """
        Se cambio la lógica para adaptarse a la subclase 
        Sigue teniendo el mismo fin (ayudar al usuario a ver graficamente la matriz)
        Pero esta vez muestra las filas que puede elegir para mutar
        Las filas se muestran segun el sentido elegido
        """
        matriz = [
            ["------", "------", "------", "Fila:1", "Fila:2", "Fila:3"],
            ["------", "------", "Fila:1", "Fila:2", "Fila:3", "Fila:4"],
            ["------", "Fila:1", "Fila:2", "Fila:3", "Fila:4", "Fila:5"],
            ["Fila:1", "Fila:2", "Fila:3", "Fila:4", "Fila:5", "------"],
            ["Fila:2", "Fila:3", "Fila:4", "Fila:5", "------", "------"],
            ["Fila:3", "Fila:4", "Fila:5", "------", "------", "------"]
        ]
        if self.direccion == 1:# Sentido ascente
            self.separar()
            print("\n".join("  ".join(matriz[i][j] for j in range(6)) for i in range(6)))
        else:
            # Sentido descendente
            matriz = self.revertir(matriz) # Se revierte la matriz
            self.separar()
            print("\n".join("  ".join(matriz[i][j] for j in range(6)) for i in range(6)))

    def revertir(self,matriz: list) -> list:
        """
        Método que retorna una versión revertida de las sublistas de la matriz
        """
        return [list(reversed(sublista)) for sublista in matriz]

    def elegir_filas(self) -> list:
        """
        Se le pide al usuario que igrese la fila que desea mutar
        Si el input corresponde al formato retornara e imprimira
        las coordenadas de los elementos de la fila dependiendo
        el sentido (self.direccion)
        """
        while True:# Se verifica que el usuario ingrese de forma correta el input
            fila  = input("\nIngrese la fila seleccionada: (Formato: Fila:1) :  ").lower()
            # Se verfica que la entrada corresponda a las claves del diccionario de coordenadas
            if fila in self.coordenadas:
                break
            else:
                print("Ingreso incorrecto, siga el formato")
        # Retorna el valor de la clave introducida segun el sentido, la clave es una lista con coordendass
        if self.direccion == 1: # Ascendente
            print(f"Has seleccionado la {fila}. Coordenadas: {self.coordenadas[fila]}")
            return self.coordenadas[fila]
        else:
            # Descendente
            coordenadas = list(reversed(self.coordenadas[fila])) # Revierte la lista de coordenadas
            print(f"Has seleccionado la {fila}. Coordenadas: {coordenadas}")
            return coordenadas

    def crear_mutante(self,adn: list,base: str,direccion: int) -> list:
        self.adn = adn
        self.base = base
        self.direccion = direccion
        """
        Método heredado modificado
        Mientras se respete el fomato este método retorna una matriz modificada
        en caso contrario se le pedira al usuario que lo intente de nuevo
        """
        while True:
            try:
                self.separar()
                print("\nElija donde quiere generar el mutante diagonal")
                print("Mutante Ascendente") if self.direccion == 1 else print("\nMutante Descendente")# Muestra la dirección del usuario
                self.mostrar_coordenadas()
                self.separar()
                # Se llama al método para determinar con que coordenadas trabajar
                secuencia =self.elegir_filas()

                # Pedir las coordenadas desde donde se inicia la mutación
                origen = list(input("\nIngrese la coordenada (fila, columna. Ej: 21): "))
                origen = list(map(int, origen))
                if origen not in secuencia and len(origen) != 2:# Se crea una instancia de error si se la entrada es diferente al formato
                    raise ValueError("\nIngrese solamente el par de coordenadas dentro de la fila")
                inicio = secuencia.index(origen)# Se guarda el indice perteneciente al origen introducido
                
                # Cambia los valores de las coordenadas de la matriz por la base ingresada por el usuario
                for i in range(self.cantidad):
                    fila, columna = secuencia[inicio + i]
                    self.adn[fila][columna] = self.base
                
                # Según la dirección se invierte la matriz o no
                if self.direccion == 1:
                    return self.adn
                else:
                    adn = self.adn
                    return self.revertir(adn)# Retorna una versión revertida de la matriz

                # Razones para pedir al usuario que lo intente devuelta
            except ValueError as error:# Ingresar mal los datos
                self.limpiar_consola()
                self.separar()
                print(f"\nError. {error}")
            except IndexError:# Ingresar un origen que produzca iterar fuera de la matriz
                self.limpiar_consola()
                self.separar()
                print("\nError: Fuera de rango de la matriz | RECUERDE: la base se repite 4 veces dentro del rango de la fila")