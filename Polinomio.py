def eval_polinomio_bruto(coeficientes, x):
    resultado = 0
    n = len(coeficientes) - 1
    for i in range(n + 1):
        resultado += coeficientes[i] * (x ** (n - i))
    return resultado

# Ejemplo de uso:
coeficientes = [2, -3, 5, 0]  # Representa el polinomio 2x^3 - 3x^2 + 5x + 0
x0 = 2
resultado = eval_polinomio_bruto(coeficientes, x0)
print(f"El valor del polinomio en x0={x0} es {resultado}")

def eval_polinomio_horner(coeficientes, x):
    resultado = 0
    for coef in coeficientes:
        resultado = resultado * x + coef
    return resultado

# Ejemplo de uso:
coeficientes = [2, -3, 5, 0]  # Representa el polinomio 2x^3 - 3x^2 + 5x + 0
x0 = 2
resultado = eval_polinomio_horner(coeficientes, x0)
print(f"El valor del polinomio en x0={x0} es {resultado}")
