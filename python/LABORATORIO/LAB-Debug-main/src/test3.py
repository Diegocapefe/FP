## Error en tiempo de ejecución: Error de tipos
import random
def generar_aleatorios(limite_inf, limite_sup, num_aleatorios):
    aleatorios= []
    for _ in range(num_aleatorios):
        aleatorios.append(random.randint(limite_inf,limite_sup))
    return aleatorios   

if __name__== "__main__":
    lim_inf, lim_sup, num = 2, 100, 5
    print("Generando " + str(num) + "números entre "+ str(lim_inf) + " y " + str(lim_sup) )#no se pueden concatenar int con stting a menos que parseemos los int o que usemos f""
    print(generar_aleatorios(lim_inf, lim_sup, num))