def fibonacci(value):
    sum=1
    resultado=0
    while sum!=value:
        resultado=resultado+sum
        sum+=1
    return resultado
        
def fibonacci_lista(value):
    values=[0,1]
    for _ in range(value-1):
        values.append(values[-1]+values[-2])
    return values[value]

def fibonacci_2(value):
    anterior,resultado=0,1
    for i in range(value-1):
        anterior, resultado=resultado,anterior + resultado
    return resultado

def fibonacci_recursivo(value):
    if value in (0,1):
        return value
    return fibonacci_recursivo(value-1)+fibonacci_recursivo(value-2)

