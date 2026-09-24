# ## 📌 Ejercicio 4: Tabla de tiempos (`viaje_ej4.py`)

# Muestra cuánto se tarda en llegar a Marte (225 millones de km) con velocidades de 10.000 a 50.000 km/h (en saltos de 10.000 km/h), usando `for` y `range()`:

# ```python
# # Salida esperada:
# Velocidad: 10000 km/h -> Tiempo: 937.5 días
# Velocidad: 20000 km/h -> Tiempo: 468.75 días


# Distancia a Marte en km
distancia_marte = 225000000

# Bucle desde 10.000 hasta 50.000 km/h (incluido), en saltos de 10.000
for velocidad in range(10000, 50001, 10000):
    tiempo_horas = distancia_marte / velocidad
    tiempo_dias = tiempo_horas / 24
    
    print(f"Velocidad: {velocidad} km/h -> Tiempo: {tiempo_dias} días")

