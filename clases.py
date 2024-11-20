import random
import os

class Detector:
    """
    Esta es la clase detector que verifica por cada dirección
    de la matriz si existen mutantes
    """
    # Valores que son necesarios para detectar mutantes
    CANTIDAD_MAXIMA = 3 # Maximo de bases iguales
    rango_secuencia = 6 # Rango de las secuencias introducidas
    coordenadas = {# Coordendas para iterar en diagonal
    "d1" : [(3, 0), (2, 1), (1, 2), (0, 3)],
    "d2" : [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)],
    "d3" : [(5, 0), (4, 1), (3, 2), (2, 3), (1, 4), (0, 5)],
    "d4" : [(5, 1), (4, 2), (3, 3), (2, 4), (1, 5)],
    "d5" : [(5, 2), (4, 3), (3, 4), (2, 5)]
    }

# Método constructor donde se define la referencia de la matriz
# y también un contador de bases
    def __init__(self,adn: list) -> None:
        self.adn = adn
        self.contador = 1

# Metodo principal que llama al metodo gestor
    def detectar_mutantes(self) -> bool:
        return self.mutantes()
    

    def mutantes(self) -> bool:# Metodo que gestiona las distintas direciones
        """
        Retorno True = Existen mutaciones en alguna dirección
        Retorno False = No existen mutaciones en ninguna dirección
        """
        if  self.direcciones("horizontal") or self.direcciones("vertical") or self.direcciones("diagonal") or self.direcciones("diagonal.invertida"):
            return True
        else:
            return False
        
    def verficacion(self, lista: list, rango: int) -> bool: #Metodo de verificación
        # Inicializa lo valores a trabajar
        self.identidad = lista
        self.rango = rango
        """
        Si contador no supera la cantidad maxima retorna false
        """
        for j in range(1, self.rango):# Bucle que itera sobre la lista
            """ Condición de verificación de lista
            Se evalua si se repiten bases más de 3 veces"""
            if self.identidad[j] == self.identidad[j-1]:# Verifica si un elemento es igual a su anterior
                self.contador += 1 # Si es igual, contador aumenta en 1 
            else:
                self.contador = 1 # Si no es igual, contador vuelve a 1

            if self.contador > self.CANTIDAD_MAXIMA: # Verifica si contador es mayor a la cantidad maxima aceptable
                return True
        return False

    def direcciones(self, direccion: str) -> bool:
        """
        Crea una lista segun la dirección y la verifica
        """
        if direccion == "horizontal":
            secuencias = [self.adn[fila] for fila in range(self.rango_secuencia)]
        elif direccion == "vertical":
            secuencias = [[self.adn[fila][columna] for fila in range(self.rango_secuencia)] for columna in range(self.rango_secuencia)]
        elif direccion == "diagonal":
            secuencias = self.diagonales(1)
        elif direccion == "diagonal.invertida":
            secuencias = self.diagonales(2)
        for secuecia in secuencias:# Verifica
            if self.verficacion(secuecia,len(secuecia)):
                return True
        return False

    def diagonales(self,control: int) -> list:
        """
        Genera todas las diagonales de la matriz segun las coordenadas (ascendentes y descendentes).
        """
        diagonales = []
        if control == 1:
            for i in self.coordenadas.values():
                diagonales.append([self.adn[x][y] for x, y in i])
        else: 
            matriz = self.adn
            matriz = [list(reversed(sublista)) for sublista in self.adn]
            for j in self.coordenadas.values():
                diagonales.append([matriz[x][y] for x, y in j])
        return diagonales