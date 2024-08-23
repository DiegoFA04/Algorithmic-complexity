from itertools import permutations

def es_solucion(valores):
    s = valores['S']
    e = valores['E']
    n = valores['N']
    d = valores['D']
    m = valores['M']
    o = valores['O']
    r = valores['R']
    y = valores['Y']
    
    send = s * 1000 + e * 100 + n * 10 + d
    more = m * 1000 + o * 100 + r * 10 + e
    money = m * 10000 + o * 1000 + n * 100 + e * 10 + y
    
    return send + more == money

def fuerza_bruta():
    letras = 'SENDMOREY'
    digitos = range(10)
    
    for perm in permutations(digitos, len(letras)):
        valores = dict(zip(letras, perm))
        if valores['M'] == 0:  # M no puede ser 0 ya que es el primer dígito de MONEY
            continue
        if es_solucion(valores):
            return valores
    return None

resultado = fuerza_bruta()
if resultado:
    print(f"Solución encontrada: {resultado}")
else:
    print("No se encontró solución.")
