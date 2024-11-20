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
