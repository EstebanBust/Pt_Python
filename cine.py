def rellenar():
    filas = 10
    columnas = 10
    asientos = [["L" for _ in range(columnas)]for _ in range(filas)]
    return asientos


def imprimir_matriz(matriz):
    nFila = 1
    nCol = 1
    print(" ", end="\t")
    for _ in matriz:
        print("C", nCol, end="\t")
        nCol += 1
    print()
    
    for fila in matriz:
        print("F", nFila, end="\t")
        nFila += 1
        for elemento in fila:
            print(elemento, end='\t')
        print()


matriz_asientos = rellenar()

while True:
    print("Estado de asientos")
    imprimir_matriz(matriz_asientos)

    opcion = input("Ingrese la fila del asiento, o presione 'S' para salir.")

    if opcion.lower() == "s":
        print("Programa cerrado por el usuario.")
        break
    else:
        try:
            fila = int(opcion) - 1
            opcion2 = input("Ingresa el numero de columna")
            try:
                columna = int(opcion2) - 1
                if matriz_asientos[fila][columna] == "L":
                    matriz_asientos[fila][columna] = "O"
                    print("asiento asignado exitosamente")
                else:
                    print("EL ASIENTO ESTA OCUPADO, INTENTALO NUEVAMENTE!!")

            except ValueError:
                print("Solamente se admiten numeros de columna")

        except ValueError:
            print("Ingresa un numero de fila o la 'S' para salir")
