
distancia_km = int(input("Inserte la distancia en km: "))  # distancia Tierra - Luna
velocidad_kmh = int(input("Inserte la velocidad en kmh: "))
tiempo_horas = distancia_km / velocidad_kmh
tiempo_dias = tiempo_horas / 24
print(f"Tardarías {tiempo_dias} días en llegar.")

