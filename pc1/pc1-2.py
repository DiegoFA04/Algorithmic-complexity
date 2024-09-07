def algortimo(lista, objetivo):

    if len(lista) == 0:
        return False

    pivote = len(lista) // 3

    if lista[pivote] == objetivo:

        return True

    elif lista[pivote] > objetivo:

        return algortimo(lista[:pivote], objetivo)

    elif lista[pivote * 2] == objetivo:

        return True

    elif lista[pivote * 2] > objetivo:

        return algortimo(lista[pivote:pivote * 2], objetivo)

    else:

        return algortimo(lista[pivote * 2:], objetivo)
    
    
lista = [2, 5, 8, 10, 13, 15, 18, 20]
elemento = 15

print(algortimo(lista, elemento)) # Salida: True