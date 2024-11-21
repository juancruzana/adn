from clases import *

import os

def limpiar_consola() -> None:
    # Limpia la consola según el sistema operativo.
    os.system('cls' if os.name == 'nt' else 'clear')

def imprimir_secuencia(adn: list) -> None:
    # Imprime la matriz de ADN de forma legible.
    print("\n".join("  ".join(fila) for fila in adn), "\n")

def verificar_opciones(mensaje: str, opciones: tuple, limite: int) -> int:
    # Verifica que el usuario ingrese una opción válida basada en las opciones y su longitud.
    while True:
        try:
            opcion = input(mensaje)
            if opcion in opciones and len(opcion) == limite:
                return int(opcion)
            print("\nOpción inválida. Intente nuevamente.")
        except ValueError:
            print("\nPor favor, ingrese un número válido.") 

def mutar(adn: list) -> list:
    # Instancia objetos de las clases Radiación o Viruz para modificar el ADN.
    while True:
        base = input("Ingrese la base nitrogenada que desea para generar la mutación: ").upper()
        if base in ["A", "C", "G", "T"]:  # Valida que la base esté permitida.
            break
        print("\nBase inválida. Intente nuevamente.")

    # Selección de tipo de mutación
    opcion = verificar_opciones("\n¿Cómo desea mutar? \nHorizontal: 1 \nVertical: 2 \nDiagonal: 3\n: ", ("1", "2", "3"), 1)
    
    if opcion in [1, 2]:
        mutante = Radiacion()
        print("Mutante Horizontal") if opcion == 1 else print("Mutante Vertical")
        mutante.mostrar_coordenadas()
        posicion_inicial = input("Ingrese la coordenada inicial (Fila, Columna. Ej: 21): ")
        adn = mutante.crear_mutante(adn, opcion, base, posicion_inicial)
    else:
        sentido = verificar_opciones("\n¿En qué sentido desea la mutación diagonal?\nAscendente: 1 | Descendente: 2\n: ", ("1", "2"), 1)
        print("Mutante Ascendente") if sentido == 1 else print("Mutante Descendente")
        mutante = Viruz()
        mutante.mostrar_coordenadas(sentido)
        mutante.fila()
        posicion_inicial = input("Ingrese la coordenada inicial (Fila, Columna. Ej: 21): ")

        adn = mutante.crear_mutante(adn, base, posicion_inicial)

    imprimir_secuencia(adn)
    return adn

def sanar(adn: list) -> list:
    # Instancia la clase Sanador para corregir mutaciones en el ADN.
    sanador = Sanador(adn)
    adn = sanador.sanar_mutantes()
    imprimir_secuencia(adn)
    return adn

def detectar(adn: list) -> list:
    # Instancia la clase Detector para identificar mutaciones en el ADN.
    detector = Detector(adn)
    if detector.detectar_mutantes():
        print("\nLa secuencia de ADN contiene mutaciones.\n")
        opcion = verificar_opciones("¿Qué acción desea realizar?\nMutar ADN: 1 | Sanar ADN: 2\n: ", ("1", "2"), 1)
        return mutar(adn) if opcion == 1 else sanar(adn)
    else:
        print("\nEsta secuencia no contiene mutaciones.")
        return adn

# Bucle principal del programa
while True:
    adn = []  # Secuencia de ADN representada como matriz
    BASES_NITROGENADAS = ["A", "C", "G", "T"]  # Bases permitidas
    TAM_SECUENCIA = 6  # Tamaño de la matriz (6x6)

    print("\nDebe ingresar una secuencia de ADN.")
    print("Bases nitrogenadas permitidas: A, C, G, T.")
    
    # Entrada de la matriz de ADN
    for i in range(TAM_SECUENCIA):
        while True:
            secuencia = input(f"Ingrese la {i+1}º secuencia de 6 bases nitrogenadas: ").upper()
            if len(secuencia) == TAM_SECUENCIA and all(base in BASES_NITROGENADAS for base in secuencia):
                adn.append(list(secuencia))
                break
            print("\nSecuencia inválida. Intente nuevamente.")

    limpiar_consola()
    print("\nSecuencia de ADN ingresada:")
    imprimir_secuencia(adn)

    while True:
        print("¿Qué desea hacer?")
        opcion = verificar_opciones("Detectar mutantes: 1 | Mutar ADN: 2 | Sanar ADN: 3\n: ", ("1", "2", "3"), 1)
        
        if opcion == 1:
            adn = detectar(adn)
        elif opcion == 2:
            adn = mutar(adn)
        else:
            adn = sanar(adn)

        # Verifica si el usuario desea continuar con la misma secuencia de ADN
        continuar = verificar_opciones("¿Desea seguir usando esta secuencia de ADN?\nSí: 1 | No: 2\n: ", ("1", "2"), 1)
        if continuar == 1:
            limpiar_consola()# Llamada a la función
            print("\nEsta es la secuencia de ADN que esta usando")
            imprimir_secuencia(adn)# Llamada a la función
        else:
            break

    # Verifica si el usuario desea salir del programa
    salir = verificar_opciones("¿Desea salir del programa?\nSí: 1 | No: 2\n: ", ("1", "2"), 1)
    if salir == 1:
        break
    else:
        limpiar_consola()