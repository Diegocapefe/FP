# ### Ejercicio 5
# Defina una función ``calcula_dia_semana`` que reciba una fecha, de tipo ``date``, y devuelva el nombre 
# del día de la semana que corresponde a la fecha. **PISTA**: busca información sobre el método ``weekday()`` del tipo ``date``.

# Para probar la función, solicite al usuario que introduzca por teclado el día, mes y año de su 
# nacimiento, construya un objeto de tipo ``date``, y páselo a la función. Informe al usuario del día de la semana en que nació.
from datetime import date

diasSemana=["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado", "Domingo"]

def calcula_dia_semana(fechaDate):
    numeroSemana=date.weekday(fechaDate)
    
    return diasSemana[numeroSemana]

    # for i, dia in  enumerate(diasSemana):
    #     if i==numeroSemana:
    #         return dia
    

if __name__=="__main__":
    dia=int(input("Inserte el dia: "))
    mes=int(input("Inserte el mes: "))
    ano=int(input("Inserte el año: "))
    
    fechaFormateda=date(ano, mes, dia)
    
    diaCalculado=calcula_dia_semana(fechaFormateda)
    
    print(f"para esa fecha, el dia de la semana es: {diaCalculado}")
    