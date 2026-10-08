## Error en tiempo de ejecución: Error de valor
import random
def generar_aleatorios(limite_inf, limite_sup, num_aleatorios):
    aleatorios= []
    for _ in range(num_aleatorios):
        aleatorios.append(random.randint(limite_inf,limite_sup))
    return aleatorios   

if __name__== "__main__":
    lim_inf, lim_sup = 2, 100
    num= int(input("Indique cuántos números quiere generar\n")) 
    print(generar_aleatorios(lim_inf, lim_sup, num))