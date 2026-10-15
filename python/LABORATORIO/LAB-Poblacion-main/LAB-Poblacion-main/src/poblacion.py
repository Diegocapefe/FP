from collections import namedtuple
import csv
from matplotlib import pyplot as plt

                                #tipo               #lo que recibe
RegistroPoblacion = namedtuple('RegistroPoblacion', 'pais, codigo, año, censo')

def lee_poblaciones(ruta_fichero: str)-> list[RegistroPoblacion]:
    
    with open(ruta_fichero, "r") as fichero:
        lector=csv.reader(fichero)
        
        listaTuplas=[]
        
        #lo que recorremos es el lector no el archivo
        #el lector lee linea por linea y cada línea la guarda en una lista donde cada fila del fichero la separa por comas
        for lineaPais in lector:
            #lineaPais es esto ["pais", "XKX", "1999", "1848934"]
            pais, codigo, año, censo= lineaPais
            
            tuplaRegistroPoblacion=RegistroPoblacion(pais, codigo, año, censo)
            
            listaTuplas.append(tuplaRegistroPoblacion)
            
    return listaTuplas


def calcula_paises(poblaciones):
    paises=set()
    for registro in poblaciones:
        paises.add(registro.pais)
    return sorted(paises)

def calcula_paises_compromido(poblaciones):
    #lista de paises, ordenada alfabeticamente, sin duplicados ->[str]
    return sorted({registro.pais for registro in poblaciones})



#toma una lista de tuplas de tipo RegistroPoblacion, y el nombre o código de 
#un país, y devuelve una lista de tuplas con los datos del país que se pasa
#como parámetro (año y censo). ¡Importante!: el país puede venir expresado en
#el parámetro nombre_o_codigo con su nombre completo o con su código.
def filtra_por_pais(poblacionesListaTuplas:list[RegistroPoblacion], nombre_o_codigo: str) -> list[tuple[int,int]]:
    filtradas=[]
    for a in poblacionesListaTuplas:
        if (a.codigo==nombre_o_codigo) or (a.pais==nombre_o_codigo):
            filtradas.append((a.año, a.censo))

    return filtradas
#También se puede hacer por compresión


def filtrar_por_paises_y_anyo(poblaciones:list[RegistroPoblacion], ano:int, paises:set[str]) -> list[tuple[str, int]]:
    filtradas=[]
    for registro in poblaciones:
        #IMPORTANTE: en registro.año, año es importante que lleve año por que arriba del todo del archivo es como hemos declarado el tipo RegistroPoblacion
        #Y MUY IMPORTANTE RECORDAR PARSEAR EL AÑOOOOOO
        if int(registro.año)==ano and registro.pais in paises:
            filtradas.append((registro.pais, registro.censo))

    return filtradas


def muestra_evolucion_poblacion(poblaciones:list[RegistroPoblacion], nombre_o_codigo):
    