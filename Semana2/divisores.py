# Divisores de un Numero

n = int(input("Ingresa un numero: "))

for i in range(1,n+1):
    if n % i == 0:
        print(i)