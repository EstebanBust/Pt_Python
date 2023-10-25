lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
#sumar listas
result = lista2 + lista1
result.sort()

#encontrar minimo

def eMinimo():
    minimo = None
    for numero in result:
        if minimo == None:
            minimo = numero
        elif numero < minimo:
            minimo = numero
    return minimo

#encontrar maximo
def eMaximo():
    maximo = None
    for numero in result:
        if maximo == None:
            maximo = numero
        elif numero > maximo:
            maximo = numero
    return maximo

#forma nativa de python
print(eMinimo())
print(eMaximo())

print(min(result))
print(max(result))

#eliminar duplicados
#agrego numeros duplciados
lista3 = [1, 2, 3, 4, 5, 6]

otroResult = result + lista3


def eliminaDuplicados():
    resultado = []
    for numero in otroResult:
        if numero not in resultado:
            resultado.append(numero)

    return resultado

print(otroResult)
print(eliminaDuplicados())
#forma mas corta nativa de python
print(list(otroResult))
print(set(otroResult))
print(list(set(otroResult)))

