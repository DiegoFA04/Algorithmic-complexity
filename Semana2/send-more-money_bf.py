'''
set
Sets are used to store multiple items in a single variable.
A set is a collection which is unordered (meaning: the items will appear in a random order), unchangeable*, and unindexed.
Do not allow duplicate values.
A set can contain different data types
* Note: Set items are unchangeable, but you can remove items and add new items.
'''

# Funcion para pasar los argumentos a una estructura "set"
# La funcion con el set nos garantizan que los elementos no esten duplicados: solo se contemplarÃ¡n las letras que participan en la criptoaritmetica   
def distinct(*args):
    return len(set(args)) == len(args)

def send_more_money_FB():
    for s in range(1, 10):
        for e in range(0, 10):
            for n in range(0, 10):
                for d in range(0, 10):
                    for m in range(1, 10):
                        for o in range(0, 10):
                            for r in range(0, 10):
                                for y in range(0, 10):
                                    if distinct(s, e, n, d, m, o, r, y):
                                        send = 1000 * s + 100 * e + 10 * n + d
                                        more = 1000 * m + 100 * o + 10 * r + e
                                        money = 10000 * m + 1000 * o + 100 * n + 10 * e + y
                                        if send + more == money:
                                            print("Solucion (send, more, money) = ")
                                            return send, more, money



send_more_money_FB()


# OUTPUT
# Solucion (send, more, money) = 
# (9567, 1085, 10652)