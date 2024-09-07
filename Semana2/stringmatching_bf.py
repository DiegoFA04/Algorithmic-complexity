def strmatch(cadena, subcad):
    n = len(cadena) #Longitud de Cadena
    m = len(subcad) #Longitud de Subcadena buscada
    results = []
    for i in range(n - m):
        if subcad == cadena[i:i+m]:
            results.append(i) #Se agrega indice a la lista "results"

    return results


print("Posicion Inicial de la Subcadena: ", strmatch("abracadabracalamzoo", "rac"))