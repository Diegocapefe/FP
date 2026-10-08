def cargar_palabras(ruta):
        ''' 
        Recibe la ruta de un fichero de texto que contiene una palabra por línea y devuelve
        dichas palabras en una lista.    
        
        :param ruta: Ruta de un fichero de texto. El fichero debe contener una palabra por línea.
        :type ruta: str
        :return: Una lista con las palabras leías del fichero
        :rtype: list[str]
        '''
        
        with open(ruta, encoding='utf-8') as f:
            res = []
            for linea in f:
                res.append(linea.strip()) # strip() elimina los espacios en blanco y saltos de línea al principio y al final
            return res
        
   
#RANDOM NO SE IMPORTA CON EL FROMMMM
import random
def elegir_palabra(listaPalabras: list):
    '''
    Elige la palabra a adivinar:
    - Selecciona una palabra aleatoria de la lista 'palabras'
    - Devuelve la palabra seleccionada
    Ayuda: 
    - La función 'random.choice' del paquete 'random' recibe una lista de opciones y 
      devuelve una de ellas seleccionada aleatoriamente.

    :param palabras: Lista con las palabras a seleccionar
    :type palabras: list[str]
    :return: La palabra seleccionada
    :rtype: str
    '''
    
    opcionRandom = random.choice(listaPalabras)
    
    return opcionRandom
    
    
    
def enmascarar_palabra(palabraAadivinar, letras_probadas):
    '''
    Enmascarar la palabra:
    - Inicializar una lista vacía. 
    - Recorrer cada letra de la palabra, añadiendola a la cadena resultado 
      si forma parte de las letras_probadas, o añadiendo un '_' en caso contrario. 
    - Devuelve una cadena con la palabra enmascarada.
    
    :param palabra: Palabra que se quiere enmascarar
    :type palabra: str
    :param letras_probadas: Conjunto con las letras que ya se han probado
    :type letras_probadas: set[str]
    :return: La palabra original en la que las letras que no se han probado
       aparecen enmascaradas con un _.
    :rtype: str
    '''
    
    #usamos una lista en vez de un conjunto porque:
    # 1. las listas son ordenadas y los conjuntos no
    # 2. los elementos en los conjuntos no se pueden repetir

    respuesta=""
    for letra in palabraAadivinar:
        
        if letra in letras_probadas:
            respuesta+=letra
            
        else:
            respuesta+="-"

    return respuesta


#esta mal, hay que mirar el readme y el string de cada funcion
def pedir_letra(letras_probadas):
    '''
    Pedir la siguiente letra:
    - Pedirle al usuario que escriba la siguiente letra por teclado
    - Comprobar si la letra indicada es válida (tiene un solo caracter, es un caracter alfabético y no es una de las letras ya introducidas)
    - Mientras que la letra introducida no sea una letra válida, mostrar un mensaje de error y volver a pedir la letra
    - Considerar las letras en minúsculas aunque el usuario las escriba en mayúsculas
    - Devolver la letra
    Ayuda:
    - La función 'input' permite leer una cadena de texto desde la entrada estándar
    - El método 'lower' aplicado a una cadena devuelve una copia de la cadena en minúsculas
    - Defina dos funciones auxiliares:
        * letra_valida, que dado el conjunto de letras probadas y la letra introducida,
          devuelve True si la letra es válida, y False en caso contrario.
        * mensaje_error, que dados el conjunto de letras probads y una letra, devuelve un mensaje de error indicando,
          el motivo por el que la letra no es válida. Los mensajes de error deben ser:
               -  "Solo puedes introducir una letra. ", no tiene exactamente un caracter.
               -  "Debes introducir un carácter alfabético. ", si no introduce una letra.
               -  "Ya has introducido esa letra antes. ", si el problema es que ya introdujo esa letra.
    else:
        msg = "Ya has introducido esa letra antes. "
    :param letras_probadas: Conjunto con las letras que ya se han probado
    :type letras_probadas: set[str]
    :return: La letra que el usuario quiere probar
    :rtype: str
    '''
    
    
    letraNueva=input("Inserte una letra: ")
    while letraNueva in letras_probadas:
        letraNueva=input("Ya has probado con esa letra, inserte otra letra: ")
        
    return letraNueva



def comprobar_letra(palabra_secreta, letra):
    '''   
    Comprobar letra:
    - Comprobar si la letra está en la palabra secreta o no
    - Devolver True si estaba y False si no

    :param palabra_secreta: Palabra que se intenta adivinar
    :type palabra_secreta: str
    :param letra: letra que ha introducido el usuario
    :type letra: str
    :return: True si la letra está en la palabra
    :rtype: bool
    '''
    return letra in palabra_secreta


def mostrar_mensaje (acierto):
    '''
    Mostrar mensaje:
     - Muestra por la consola el mensaje "¡Bien hecho! Esa letra está en la palabra.",
    si acierto tiene el valor True. 
    -  Muestra por la consola el mensaje "Lo siento, esa letra no está en la palabra."
    si acierto tiene el valor False.

    :param acierto: Es True si el usuario ha acertado la letra, y False en caso contrario
    :type acierto: bool
    '''
    if acierto==True: return print("¡Bien hecho! Esa letra está en la palabra.")
    else: return print("Lo siento, esa letra no está en la palabra.")
    
    
def comprobar_palabra_completa(palabra_secreta, letras_probadas):
    '''
    Comprobar si se ha completado la palabra:
    - Comprobar si todas las letras de la palabra secreta han sido propuestas por el usuario
    - Devolver True si es así o False si falta alguna letra por adivinar
    :param palabra_secreta: Palabra que se tiene que adivinar
    :type palabra_secreta: str
    :param letras_probadas: Conjunto con las letras que ya se han probado
    :type letras_probadas: set[str]
    :return: Devuelve True si se han adivinado todas las letras de la palabra, y False en caso contrario
    :rtype: bool
    '''
    
    for letra in palabra_secreta:
        
        if letra in letras_probadas:
            