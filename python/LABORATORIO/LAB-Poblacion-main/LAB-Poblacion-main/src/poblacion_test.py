from poblacion import *

if __name__ == "__main__":
    datos=lee_poblaciones("../data/population.csv")#devuelve una lista de tuplas de tipo RegistroPoblación
    
    print(filtrar_por_paises_y_anyo(datos, 2025, {"Spain", "Portugal", "France", "Mexico", "China"}))