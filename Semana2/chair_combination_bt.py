def back(nivel, n, cola, pila):
    #Condicion de Fin
    if(nivel==n):
        print("pila", pila)
    else:
        j = nivel
        while( j < n ):
            # RESTRICCION
            if (not((nivel == 1 and cola[0] == "a") or (nivel == 0 and cola[0] == "r"))): # Si no aplica la Restriccion
                # cola.pop(0): saca el primer elemento de la cola
                pila.append(cola.pop(0))
                back(nivel+1, n, cola, pila)
                cola.append(pila.pop())
            else: # Si aplica la RestricciÃ³n
                cola.append(cola[0])
                cola.pop(0)
                
            j = j + 1


def main():
    cola = ["a", "n", "r"]  # Lista de elementos a permutar
    pila = []               # Lista para mostrar las permutaciones 
    
    nivel = 0
    n = len(cola)
    
    back(nivel, n, cola, pila)


main()