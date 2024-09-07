def f(x):
    respuesta = 0
    
    for i in range(x):
        respuesta += x
    
    for i in range(10):
        respuesta += 1
        
    for i in range(x):
        for j in range(x):
            respuesta += 1
    
    return respuesta

