## DESAFÍO DE DEPURACIÓN A CIEGAS
# Este programa contiene 2 errores lógicos ocultos.
# Usa el debugger (breakpoints, watch y paso a paso) para encontrarlos.

def es_primo(numero):
    """Devuelve True si un número es primo, False en caso contrario."""
    res = True
    if numero > 1:
        # Bucle para comprobar divisores
        for i in range(2, numero):
            if numero % i == 0:
                res = False  
                break
    return res # ERROR LÓGICO 1: ¿Qué debe devolver si encuentra un divisor?

def obtener_primos_en_rango(inicio, fin):
    """Devuelve una lista con todos los números primos en el rango [inicio, fin)."""
    primos = []
    for num in range(inicio, fin):
        if es_primo(num):
            primos.append(num)
    return primos

def main():
    inicio = 1
    fin = 10
    
    print(f"Buscando números primos entre {inicio} y {fin}...")
    primos_encontrados = obtener_primos_en_rango(inicio, fin)
    
    # Resultado esperado entre 1 y 10: [2, 3, 5, 7]
    print(f"Resultado obtenido: {primos_encontrados}")

if __name__ == "__main__":
    main()