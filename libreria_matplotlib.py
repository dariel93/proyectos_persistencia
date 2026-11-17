import matplotlib.pyplot as plt
import streamlit as st

# Grafico de barras para mostrar el consumo eléctrico mensual
"""meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"] 
consumo = [120, 150, 135, 180, 160] 
plt.bar(meses, consumo) 
plt.title("Consumo eléctrico mensual") 
plt.xlabel("Mes") 
plt.ylabel("Consumo (kWh)") 
plt.show() """

# Grafico de pastel para mostrar la distribución del consumo de energía en diferentes edificios
"""edificios = ["Oficinas", "Almacén", "Fábrica", "Tienda"] 
consumo = [350, 220, 580, 190] 
plt.pie(consumo, labels=edificios,autopct="%1.1f%%") #muestra los porcentajes dentro del grafico
plt.title("Distribución del consumo") 
plt.show() """

# Grafico de lineas para mostrar la comparativa de consumo entre dos instalaciones
"""meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"] 
instalacion_a = [120, 150, 135, 180, 160] 
instalacion_b = [100, 130, 145, 155, 170] 
plt.plot(meses, instalacion_a, marker="o", label="Instalación A") 
plt.plot(meses, instalacion_b, marker="s", label="Instalación B") 
plt.title("Comparativa de consumo") 
plt.xlabel("Mes") 
plt.ylabel("Consumo (kWh)") 
plt.legend() 
plt.grid(True) 
plt.show()"""


 
meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo"] 
consumo = [120, 150, 135, 180, 160] 
plt.bar(meses, consumo) 
plt.title("Consumo eléctrico mensual") 
plt.xlabel("Mes") 
plt.ylabel("Consumo (kWh)") 
st.pyplot(plt) 

edades = [ 
18, 19, 20, 21, 22, 
23, 24, 25, 25, 26, 
27, 28, 29, 30, 31, 
32, 35, 38, 42, 45 
] 
plt.title("Distribución de edades") 
plt.xlabel("Edades") 
plt.ylabel("Personas") 
plt.hist(edades,bins=5,edgecolor="black") 
plt.show()