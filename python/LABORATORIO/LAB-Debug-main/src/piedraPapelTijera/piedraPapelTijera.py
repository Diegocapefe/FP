import random

def ordenador_decide_jugada():
    ''' 
    Elige aleatoriamente entre piedra, papel o tijeras y devuelve la elección.     
    '''
    opciones = ["piedra", "papel", "tijeras"]
    res = random.choice(opciones)
    return res


def usuario_decide_jugada():
    ''' 
    Pide al usuario que elija entre piedra, papel o tijeras y devuelve la elección.     
    '''
    eleccion_usuario = input("Elige piedra, papel o tijeras: ")
    while eleccion_usuario not in ["piedra", "papel", "tijeras"]:
        eleccion_usuario = input("Opción no válida, por favor elige piedra, papel o tijeras: ")
    return eleccion_usuario

def determina_ganador(jugada_usuario, jugada_ordenador):
    res = None
    if jugada_usuario == jugada_ordenador:
        res = 0
    elif jugada_usuario == "piedra" and jugada_ordenador == "tijera":
        res = 1
    elif jugada_usuario == "tijera" and jugada_ordenador == "papel":
        res = 1
    elif  jugada_usuario == "papel" and jugada_ordenador == "piedra":
        res = 1
    else:
        res = -1
    return res



def jugar_ronda():
    print("Bienvenido: ")
    ordenador=ordenador_decide_jugada()
    usuario=usuario_decide_jugada()
    
    print(f"ordenador a elegido {ordenador} y el usuario ha elegido {usuario}")
    
    resultado=determina_ganador(usuario, ordenador)
    if resultado==-1:
        print("Ganador es ordenador")
    if resultado==1:
        print("Ganador es usuario")
    if resultado==0:
        print("Ganador es empate")
        
    
    
if __name__ == "__main__":
    jugar_ronda()