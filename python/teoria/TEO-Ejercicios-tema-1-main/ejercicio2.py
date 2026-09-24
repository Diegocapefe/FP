
### Ejercicio 2
#Defina una función ``calcula_estado_nutricional`` que reciba como parámetros el peso y la estatura de 
# una persona (en kilogramos y metros, respectivamente), y devuelva una cadena de texto con el estado 
# nutricional de la persona de acuerdo con su IMC. El estado nutricional puede ser uno de los siguientes:
#- Bajo peso: imc < 18.5
#- Normal: 18.5 <= imc < 25
#- Sobrepeso: 25 <= imc < 30
#- Obesidad: imc >= 30

from ejercicio1 import calcula_imc

def calcula_estado_nutricional(kg, metros):
    
    imc=calcula_imc(kg, metros)
    
    if imc<18.5:
        return "Bajo peso"
    
    if imc<=25:
        return "Normal"
    
    if imc<=25:
        return "Sobrepeso"
    
    if imc>=3:
        return "Obesidad"
    
    
if __name__ == "__main__":
    #input devuelve un string
    peso=int(input("inserte su masa corporal en kg: "))
    altura=float(input("inserte su altura en metros: "))

    print(calcula_estado_nutricional(peso, altura))