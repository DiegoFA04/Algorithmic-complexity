def min_repeats_to_substring(a, b):
    # Comenzamos repitiendo la cadena 'a' al menos hasta cubrir la longitud de 'b'
    repeated_a = a
    count = 1
    
    # Mientras la longitud de la cadena repetida sea menor que la longitud de 'b', se repite más veces
    while len(repeated_a) < len(b):
        repeated_a += a
        count += 1
    
    # Si 'b' es subcadena de la repetición actual de 'a', se devuelve el número de repeticiones
    if b in repeated_a:
        return count
    
    # Probar repitiendo una vez más
    repeated_a += a
    count += 1
    
    # Si 'b' es subcadena de la repetición adicional, devolver el número de repeticiones
    if b in repeated_a:
        return count
    
    # Si no llega a ser subcadena, se devuelve -1
    return -1

# Ejemplos:
print(min_repeats_to_substring("abc", "cab"))  # Salida: 2
print(min_repeats_to_substring("abcd", "cdabcdab"))  # Salida: 3
print(min_repeats_to_substring("aat", "b"))  # Salida: -1

# Implementé fuerza bruta, ya que el problema no requiere un enfoque tan complejo sino más directo
# Simplemente se repite la cadena 'a' hasta que cubra la longitud de 'b' y se verifica 
# si 'b' es subcadena. La complejidad O(n×m), donde n es la longitud de a y m la longitud de b