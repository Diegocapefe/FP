### Ejercicio 4
# Defina una función ``lee_numeros`` que lea varios números enteros del teclado y los devuelva almacenados en una lista. 
# La cantidad de números a leer será un parámetro de la función.

# Pruebe la función ``lee_numeros`` pidiéndole que lea tantos números como indique el usuario por el teclado, 
# y mostrando en la consola la lista resultante. A continuación, implemente los siguientes cálculos sobre la lista 
# obtenida, mostrando el resultado de cada uno por consola:

# - Mayor número de la lista (**PISTA**: Busque una función predefinida de Python que realiza este cálculo)
# - Media de los números de la lista (si la lista estuviera vacía, se mostraría "No es posible calcular la media")
# - Número de elementos pares en la lista
# - Nueva lista con aquellos elementos de la lista leída que sean mayores a 10

def lee_numeros(cantidad):
    lista=[]
    for i in range(cantidad):
        lista.append(int(input("Inserte un número: ")))
        
    return lista


cant=int(input("inserte la cantidad de números que desea introducir: "))
numeros=lee_numeros(cant)


# - Media de los números de la lista (si la lista estuviera vacía, se mostraría "No es posible calcular la media")
# - Número de elementos pares en la lista
# - Nueva lista con aquellos elementos de la lista leída que sean mayores a 10
print(f"El número maximo de la lista es {max(numeros)}")

sumaNumeros=0
numerosPares=0
listaMayoresDeDiez=[]
for numero in numeros:
    sumaNumeros+=numero
    if numero % 2 ==0:
        numerosPares+=1
        
    if numero > 10:
        listaMayoresDeDiez.append(numero)
media=sumaNumeros/len(numeros)
print(f"La media de todos los numeros introducdidos es: {media}.")
print(f"En total hay {numerosPares} numeros pares.")
print("La lista de los numeros mayores de 10 es: ")
if len(listaMayoresDeDiez) < 1:
    print(0)
else:
    for numero2 in listaMayoresDeDiez:
        print(numero2)
    


