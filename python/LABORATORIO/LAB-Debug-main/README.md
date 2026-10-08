# LAB-Debug: Identificación de Errores y Depuración en Python

Autor: Toñi Reina

Este repositorio contiene un conjunto de experimentos de laboratorio diseñados para aprender a identificar, clasificar y corregir los distintos tipos de errores en programas escritos en Python, así como para dominar el uso del **debugger**.

---

## 🎯 1. Objetivos de la actividad

1. Reconocer y diferenciar los tres grandes tipos de errores en programación: **sintácticos**, **en tiempo de ejecución** y **lógicos**.


2. Interpretar la salida del intérprete de Python (trazas de error o *Tracebacks*).


3. Utilizar la estrategia clásica de inserción de `print` para rastrear errores de lógica.


4. Aprender a utilizar las herramientas de un **depurador (*debugger*)** profesional (puntos de parada o *breakpoints*, inspección de variables y control de flujo de ejecución).



---

## 📋 2. Hoja de registro de errores (Instrucciones)

A medida que vayas ejecutando cada archivo en los siguientes bloques, **analiza la salida de la terminal y completa la siguiente tabla en tu cuaderno de prácticas o informe antes de pasar al siguiente archivo**:

| Archivo | Tipo de Error (Sintáctico / Ejecución / Lógico) | Línea exacta del fallo | Excepción / Mensaje del intérprete | Causa del problema y solución aplicada |
| --- | --- | --- | --- | --- |
| `test1.py` | Sintáctico | Línea 4 | `SyntaxError: expected ':'` | Falta `:` al final del `for`. |
| `test2.py` |  NameError: | Línea 5 | name 'num' is not defined. | El nombre del parametro es diferente cuando se usa |
| `test3.py` |  |  |  |  |
| `test4.py` |  |  |  |  |
| `test5.py` |  |  |  |  |
| `test6.py` |  |  |  |  |
| `test7.py` |  |  |  |  |
| `test8.py` |  |  |  |  |

---

## 🛠️ 3. Desarrollo de los experimentos

Sigue en orden las siguientes fases de trabajo ejecutando, analizando y anotando en la tabla cada archivo Python:

---

### Parte A: Errores Sintácticos (Syntax Errors)

Los errores sintácticos ocurren durante la fase de análisis del código (_parsing_), antes de que el programa llegue a ejecutarse. Se producen cuando el código escrito incumple las reglas gramaticales, la estructura o la sintaxis del lenguaje de programación.

Características principales:

* **Bloqueo previo a la ejecución**: Dado que el intérprete de Python no puede traducir el código a lenguaje máquina si la sintaxis es incorrecta, el programa no se ejecutará en absoluto (ni siquiera las líneas de código anteriores al error).

* **Detección temprana por el IDE**: La mayoría de los entornos de desarrollo (como VS Code) detectan estos errores mientras escribes, marcándolos con un subrayado rojo.

Causas más comunes:

* Estructuras de control incompletas (por ejemplo, olvidar los dos puntos : al final de un `if`, `for` o `def`).
* Delimitadores no emparejados (no cerrar un paréntesis ), corchete ], llave } o comilla " '.
* Indentación incorrecta o inconsistente (mezclar espacios y tabuladores, o indentar sin una estructura que lo requiera).
* Palabras clave mal escritas (como escribir `wile` en lugar de `while`, o `True` en minúscula).

**Archivo a examinar:** `test1.py`

**Instrucciones:**
    
1. Observa cómo el entorno de desarrollo (IDE) señala el error en el código antes de ejecutarlo.
2. Ejecuta el archivo `test1.py` en la terminal.
3. Revisa la traza mostrada (`SyntaxError: expected ':'`) y **anótala en la tabla**.
4. Corrígelo agregando los dos puntos `:` en el bucle `for`.

---

### Parte B: Errores en Tiempo de Ejecución (Runtime Errors)

A diferencia de los errores sintácticos, los errores en tiempo de ejecución ocurren cuando el código está gramaticalmente bien escrito y supera la fase de análisis inicial (_parsing_), pero se produce una condición anómala o inesperada mientras el programa se está ejecutando que el intérprete de Python no puede gestionar.

Características principales:

* **Interrupción abrupta**: El programa comenzará a ejecutarse con normalidad y completará con éxito todas las instrucciones anteriores al fallo. En el momento preciso en que alcance la línea problemática, la ejecución se detendrá de golpe.

* **Generación de excepciones**: Python detiene el programa lanzando un objeto de error denominado Excepción (por ejemplo, `NameError`, `TypeError`, `ValueError`, `IndexError`, etc.).

* **Traceback o Traza de llamadas**: El intérprete muestra en la consola una traza detallada que indica la secuencia exacta de llamadas a funciones y la línea concreta del código donde ocurrió el error, junto con un mensaje explicativo.

* **Invisibilidad previa**: Salvo en casos muy evidentes, los entornos de desarrollo (IDEs) no suelen señalar estos errores mientras escribes el código, ya que dependen de los datos que el programa recibe o manipula en el momento de la ejecución (por ejemplo, la entrada del usuario o el contenido de una lista).

Experimentos a realizar:

1. **Error de nombres (`NameError`):**

    * **Archivo:** `test2.py`

    * **Instrucciones:** Ejecuta el archivo e identifica qué variable no ha sido definida antes de su uso. Rellena la tabla.

2. **Error de tipos (`TypeError`):**

    * **Archivo:** `test3.py`

    * **Instrucciones:** Ejecuta el programa y analiza por qué falla la concatenación de texto y enteros. Anota los datos en la tabla y corrige la instrucción `print` formateando adecuadamente los enteros a cadenas.

3. **Error de valor (`ValueError`):**

    * **Archivo A (`test4.py`):** Revisa el intento de desempaquetado de variables (`lim_inf, lim_sup, num = 2, 100`) y observa la excepción por falta de valores. Anótalo en la tabla.

    * **Archivo B (`test5.py`):** Ejecuta el programa e introduce una letra (por ejemplo, `A`) cuando te pida un número. Observa cómo falla la conversión con `int()` y anótalo en la tabla.

4. **Error de índice fuera de rango (`IndexError`):**
    * **Archivo:** `test7.py`
    * **Instrucciones:** Ejecuta el programa y observa la traza al intentar acceder a `numeros[len(numeros)]`. Recuerda que en Python los índices empiezan en `0`, por lo que el último índice válido es `len(numeros) - 1`. Anota los datos del error en la tabla.

5. **Error de división por cero (`ZeroDivisionError`):**
    * **Archivo:** `test8.py`
    * **Instrucciones:** Ejecuta el archivo e introduce `0` cuando la consola pida la cantidad de números a generar. Observa la excepción al intentar calcular la media dividiendo por la longitud de una lista vacía y regístralo en la tabla.
---

### Parte C: Errores Lógicos 

Un error lógico ocurre cuando el código es sintácticamente correcto y se ejecuta de principio a fin sin lanzar ninguna excepción ni romper la aplicación, pero el comportamiento o los resultados obtenidos no coinciden con lo que el programador pretendía.   

Características principales:

* **Ejecución completa sin mensajes de error**: El intérprete de Python no detecta ningún problema porque todas las operaciones son válidas dentro del lenguaje. La terminal no mostrará ningún Traceback rojo ni aviso.   

* **Los errores más difíciles de detectar**: Al no haber llamadas de atención del IDE ni mensajes de fallo en la consola, estos errores pueden pasar desapercibidos durante mucho tiempo si no se realizan pruebas exhaustivas.   

Causas más comunes:

* Mal uso de operadores matemáticos o precedencia de operaciones (por ejemplo, omitir paréntesis al calcular un promedio).   
* Fallos en la lógica de condiciones `if` / `else` (usar > en lugar de >=, o confundir operadores lógicos `and` / `or`).
* Modificación incorrecta de variables acumuladoras o contadores dentro de un bucle.
* Devolver un valor equivocado desde una función o alterar la secuencia de pasos de un algoritmo.   

Para intentar detectar el origen del error se pueden aplicar dos estrategias:

* **Estrategia print**: Consiste en insertar mensajes `print()` temporales en puntos estratégicos para inspeccionar el valor intermedio de las variables a lo largo de la ejecución.   
* **Uso del Depurador (Debugger)**: Consiste en pausar la ejecución en tiempo real mediante puntos de parada o `breakpoints` para analizar el estado interno de las variables sin tener que modificar el código fuente.   

#### Estrategia print
* **Archivo a examinar:** `test6.py`

* **Instrucciones:**
    1. Ejecuta el código e inspecciona el mensaje impreso.
    2. ¿Es el resultado de la media realmente correcto o solo está mostrando la suma?
    3. Modifica el archivo para calcular la media real dividiendo la suma entre el número total de elementos y completa la entrada correspondiente en la tabla.

---

### Parte D: Introducción al Debugger (Depurador de Código)

Cuando un error lógico es difícil de localizar, el uso de mensajes `print` resulta insuficiente. Aquí es donde entra en juego el depurador.

* **Archivo de trabajo:** `test_debug.py`

* **Flujo del ejercicio:**

    1. **Inspección del problema:**
        * Ejecuta `test_debug.py` e introduce un número objetivo que no esté en la lista generada.
        * Observa el fallo por índice fuera de rango (`IndexError`) al no controlar el límite de la lista en la función `encontrar_numero`.

    2. **Establecer Breakpoints (Puntos de parada):**

        * Haz clic a la izquierda del número de línea dentro de `encontrar_numero` (p. ej., en la línea del bucle `while`) para añadir un punto rojo (*breakpoint*).

    3. **Ejecutar en modo depuración:**
        * Inicia el depurador (*Run and Debug*).
        * Observa cómo la ejecución se detiene en la línea seleccionada.

    4. **Inspeccionar el estado del programa:**
        * Consulta el panel de **Variables** (Locales y Globales) para ver el contenido actualizado de `lista`, `objetivo` e `indice`.
        * Añade en el panel **Watch (Inspección)** expresiones como `lista[indice]` o `lista[indice] != objetivo` para evaluarlas en tiempo real.

    5. **Controles de navegación de depuración:**
        Practica con la barra de herramientas del debugger:
            * **Continue (F5):** Continúa la ejecución hasta el siguiente punto de parada.
            * **Step Over (F10):** Ejecuta la siguiente línea de código sin entrar en las funciones.
            * **Step Into (F11):** Entra dentro de la función que se ejecuta en esa línea.
            * **Step Out (Shift + F11):** Sale de la función actual devolviendo el control al llamador.
            * **Restart / Stop:** Reinicia o finaliza la sesión de depuración.

    6. **Solución del ejercicio:**
 Modifica la función `encontrar_numero` para que valide los límites de la lista antes de acceder por índice o devuelva `-1` si el objetivo no existe. Modifica también el `main` para que muestre dos mensajes distintos, dependiendo de si el número está en la lista o no.



---

## 🏆 4. Desafío Final: Depuración a Ciegas (`desafio_debug.py`)

En el archivo `desafio_debug.py` se intenta calcular los números primos entre 1 y 13, ambos inclusive. La salida esperada es `[2, 3, 5, 7, 11, 13]`, pero al ejecutarlo verás un resultado completamente incorrecto sin que salte ningún mensaje de error.

**Tu misión:**

1. Abre `desafio_debug.py` y coloca un *Breakpoint* en el inicio de la función `main()`.
2. Utiliza los controles **Step Into (F11)** para entrar dentro de `obtener_primos_en_rango` y `es_primo`.
3. Añade la variable `numero`, la expresión `numero % i` y la lista `primos` al panel de **Watch (Inspección)**.
4. Identifica los **2 errores lógicos** que hacen que el algoritmo falle y corrígelos.

---

## 🤔 5. Cuestiones de reflexión

Responde a las siguientes preguntas tras completar las pruebas de código:

1. **Diferencia de detección:** ¿Por qué un error sintáctico impide que se ejecute **cualquier** instrucción del script, mientras que un error en tiempo de ejecución permite ejecutar las líneas previas al fallo?

2. **Diagnóstico mediante la traza (*Traceback*):** Al observar la traza de error en `test7.py` o `test8.py`, ¿qué información del mensaje te resulta más útil para localizar dónde corregir el programa?

3. **Lógica vs. Ejecución:** En `test6.py`, el programa se ejecuta completamente sin lanzar ningún mensaje de error en la terminal. ¿Por qué este tipo de errores suele ser el más peligroso al desarrollar software real?

4. **Ventajas del Debugger:** Compara la estrategia de añadir mensajes `print()` con el uso de *breakpoints* e inspección de variables en el *debugger*. ¿En qué situaciones resulta ineficiente la estrategia del `print()`?