import random

def generar_aleatorios(limite_inf, limite_sup, num_aleatorios):
    aleatorios = []
    for _ in range(num_aleatorios):
        aleatorios.append(random.randint(limite_inf, limite_sup))
    return aleatorios   

def obtener_ultimo_elemento(lista):
    return lista[len(lista)]#el error es que la lista mide 5 de tamaño pero como va de 0 a 4 al pasarle len(lista(5)) da error por que 5 no entra

if __name__ == "__main__":
    lim_inf, lim_sup, num = 2, 100, 5
    numeros = generar_aleatorios(lim_inf, lim_sup, num)
    print(f"La lista generada es: {numeros}")
    
    ultimo = obtener_ultimo_elemento(numeros)
    print(f"El último elemento es: {ultimo}")