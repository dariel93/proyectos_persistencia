import numpy as np

consumos = [1250, 1380, 980, 1450, 1520, 1100, 1600]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# 1. Consumo total semanal
# 2. Consumo media diaria
# 3. Día con mayor y menor consumo
# 4. Días con consumo superior a la media

# 6. Dias con consumo un 20% inferior a la media
# 7. Coste total , sabiendo que de lunes a viernes el coste del KW es de 0.02 y en din de semana del 0.018

consumos = np.array(consumos)
dias = np.array(dias)

# 1. Consumo total semanal
total = np.sum(consumos)
print(f"\nProducción total: {total} kWh")

# 2. Consumo media diaria
media = np.average(consumos)
print(f"Producción media: {media:.2f} kWh")

# 3. Día con mayor y menor consumo
indice_max = np.argmax(consumos)
indice_min = np.argmin(consumos)
print(indice_max)
print(indice_min)
print(f"Mayor producción: {dias[indice_max]} ({consumos[indice_max]} kWh)")
print(f"Menor producción: {dias[indice_min]} ({consumos[indice_min]} kWh)")

# 4. Días con consumo superior a la media
dias_superiores = dias[consumos > media]
print(f"Días con producción superior a la media: {dias_superiores}")

# 6. Dias con consumo un 20% inferior a la media
media_reducida = np.average(consumos)*0.8
dias_inferiores = dias[consumos < media_reducida]
print(f"Días con producción inferior a la media: {dias_inferiores}")

# 7. Coste total , sabiendo que de lunes a viernes el coste del KW es de 0.02 y en din de semana del 0.018
