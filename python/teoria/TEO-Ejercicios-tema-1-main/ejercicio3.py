### Ejercicio 3
#Defina una función ``imprime_estados_nutricionales`` que reciba como parámetro una lista de tuplas, que 
# representan el peso y la altura de una serie de personas, y muestre el IMC y el estado nutricional de 
# cada una de ellas. La salida en consola de la ejecución de la función debe ser parecida a esta:

#```python
#El IMC de la persona 1 es 23.543, y su estado nutricional es Normal.
#El IMC de la persona 2 es 27.324, y su estado nutricional es Sobrepeso.

from ejercicio1 import calcula_imc
from ejercicio2 import calcula_estado_nutricional

listaDeTuplas=[
    (73, 1.77),
    (80, 1.6), 
    (72, 1.75)
]

def improme_estados_nutricionales(listaTuplas):

    #rangue empieza en 1 no en 0
    contador=1
    for i in range(3):
        imc=calcula_imc(listaTuplas[i][0], listaTuplas[i][1])
        eNutricional=calcula_estado_nutricional(listaTuplas[i][0], listaTuplas[i][1])
        print(f"El imc de la persona {contador}  es {imc} y su estado nutricional es {eNutricional}")
        contador+=1



improme_estados_nutricionales(listaDeTuplas)
        