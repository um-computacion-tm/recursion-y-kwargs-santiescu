def sumatoria(valor):
    while valor!=0:
        resultado=resultado+valor
        valor=valor-1
    return resultado

def sumatoria_recursiva(value):
    if value!=0:
        resultado=value+sumatoria_recursiva(value-1)
        return resultado
    else: 
        return 0
    
def sumatoria_recursiva_2(value):
    #condicion de corte
    if value==0:
        return 0
    #fin condicion
    return value+sumatoria_recursiva_2(value-1)

def factorial(value):
    resultado=1
    while value>0:
        resultado=resultado*value
        value=value-1
    return resultado

def factorial_2(value):
    resultado=value
    while value>2:
        value=value-1
        resultado=resultado*value
    return resultado

def factorial_recursivo(value):
    if value<=1:
        return 1
    return value*factorial_recursivo(value-1)


print(factorial_recursivo(4))