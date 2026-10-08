## Error sintáctico
import random
def generar_aleatorios(limite_inf, limite_sup, num_aleatorios):
    aleatorios= []
    for _ in range(5):
        aleatorios.append(random.randint(limite_inf,limite_sup))
    return aleatorios   
