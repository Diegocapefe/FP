## Error lógico

import random

def encontrar_numero(lista, objetivo):
    indice = 0
    while lista[indice] != objetivo:

        indice += 1
        if indice>=len(lista):
            return False

    return indice

def generar_aleatorios(limite_inf, limite_sup, num_aleatorios):
    return [random.randint(limite_inf,limite_sup) \
                     for _ in range(num_aleatorios)]

def main():
    lista = generar_aleatorios(5, 100, 5)
    print (f"La lista generada es: {lista}")
    
    objetivo = int(input("Introduce el número que quieres encontrar: "))

    indice_encontrado = encontrar_numero(lista, objetivo)

    if indice_encontrado!=False:
        print(f"El número {objetivo} se encuentra en el índice {indice_encontrado} de la lista.")
    else:
        print ("El número se encuentra fuera del rango")

if __name__ == "__main__":
    main()