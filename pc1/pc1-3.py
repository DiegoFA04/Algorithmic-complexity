def tot_palabras_por_linea(txt):
    # Se divide el texto en líneas
    lineas = txt.split('\n')
    
    # Recursividad para contar lineas
    def contar_palabras(lineas):
        if not lineas:
            return []
        else:
            primera_linea = lineas[0]
            resto_lineas = lineas[1:]
            num_palabras = len(primera_linea.split())
            return [num_palabras] + contar_palabras(resto_lineas)
    
    # Llamar a la función recursiva interna
    return contar_palabras(lineas)

# Input
txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n Nam arcu arcu, euismod mollis rhoncus quis, egestas at leo.\n Maecenas luctus neque nulla, vel imperdiet lacus ultrices vel."

resultados = tot_palabras_por_linea(txt)
for resultado in resultados:
    print(resultado)