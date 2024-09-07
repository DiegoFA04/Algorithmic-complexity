def contar_elementos_unicos(coleccion):
    # Convertir la lista a un conjunto para eliminar duplicados
    elementos_unicos = set(coleccion)
    
    # Contar los elementos únicos
    num_unicos = len(elementos_unicos)
    
    # Retornar el número y los elementos únicos
    return num_unicos, elementos_unicos

# Ejemplo:
entrada = [1, 2, 3, 2, 1, 4, 5, 6, 4, 7,8]
num_unicos, elementos_unicos = contar_elementos_unicos(entrada)

# Mostrar resultados
print("Número de elementos únicos:", num_unicos)
print("Elementos únicos:", elementos_unicos)
