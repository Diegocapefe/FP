import random

def generar_aleatorios(limite_inf, limite_sup, num_aleatorios):
    aleatorios = []
    for _ in range(num_aleatorios):
        aleatorios.append(random.randint(limite_inf, limite_sup))
    return aleatorios   

def calcular_media(lista):
    return sum(lista) / len(lista)

if __name__ == "__main__":
    lim_inf, lim_sup, numeros = 2, 100, 0
    
    numeros = generar_aleatorios(lim_inf, lim_sup, numeros)
    media = calcular_media(numeros)
    
    print(f"Los números son {numeros} y su media es {media}")