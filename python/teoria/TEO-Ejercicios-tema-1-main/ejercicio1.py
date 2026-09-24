
### Ejercicio 1
#Defina una función ``calcula_imc`` que reciba como entrada el peso y la estatura de una persona 
# (en kilogramos y metros, respectivamente) y calcule su índice de masa 
# corporal o [IMC](https://es.wikipedia.org/wiki/%C3%8Dndice_de_masa_corporal).


def calcula_imc(kg, metros):
    
    imc=kg/((metros)**2)
    
    return imc

if __name__ == "__main__":
    #input devuelve un string
    peso=int(input("inserte su masa corporal en kg: "))
    altura=float(input("inserte su altura en metros: "))

    print(calcula_imc(peso, altura))