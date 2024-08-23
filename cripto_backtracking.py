from itertools import permutations

# Función que verifica si una asignación de dígitos a letras cumple con la ecuación SEND + MORE = MONEY
def verificar(asignacion):
    S, E, N, D, M, O, R, Y = asignacion
    send = S * 1000 + E * 100 + N * 10 + D
    more = M * 1000 + O * 100 + R * 10 + E
    money = M * 10000 + O * 1000 + N * 100 + E * 10 + Y
    return send + more == money

# Algoritmo de fuerza bruta
def fuerza_bruta():
    letras = 'SENDMORY'
    digitos = range(10)
    
    for perm in permutations(digitos, len(letras)):
        if perm[0] != 0 and perm[4] != 0:  # S y M no pueden ser 0
            if verificar(perm):
                return {letra: digito for letra, digito in zip(letras, perm)}
    return None

# Algoritmo de backtracking
def backtracking(letras, asignacion_parcial, usados):
    if len(letras) == 0:
        if verificar([asignacion_parcial[letra] for letra in 'SENDMORY']):
            return asignacion_parcial
        return None
    
    for digito in range(10):
        if digito not in usados:
            letra_actual = letras[0]
            if (letra_actual == 'S' or letra_actual == 'M') and digito == 0:
                continue  # S y M no pueden ser 0
            nueva_asignacion = asignacion_parcial.copy()
            nueva_asignacion[letra_actual] = digito
            resultado = backtracking(letras[1:], nueva_asignacion, usados | {digito})
            if resultado:
                return resultado
    
    return None

# Ejecutando los métodos
solucion_fuerza_bruta = fuerza_bruta()
print("Solución con fuerza bruta:", solucion_fuerza_bruta)

solucion_backtracking = backtracking('SENDMORY', {}, set())
print("Solución con backtracking:", solucion_backtracking)
