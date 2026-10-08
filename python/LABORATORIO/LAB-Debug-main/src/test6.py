## Error lógico
import random
def generar_aleatorios(limite_inf, limite_sup, num_aleatorios):
    aleatorios= []
    for _ in range(num_aleatorios):
        aleatorios.append(random.randint(limite_inf,limite_sup))
    return aleatorios   

if __name__== "__main__":
    lim_inf, lim_sup, num = 2, 100,5
    aleatorios=generar_aleatorios(lim_inf, lim_sup, num)
    print (f"Los números generados son {aleatorios} y su media es {(sum(aleatorios))/len(aleatorios)}")