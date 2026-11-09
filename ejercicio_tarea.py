# Dame tu presupuesto, los que sean <=  a ese presupuesto , muestra las viviendas que se puedan permitir con ese presupuesto

import csv
import streamlit as st

with open("houses.csv", "r") as f:
    viviendas = list(csv.DictReader(f))
    
    presupuesto=st.number_input("Dime tu presupuesto: ")
    
    permitidas=list(filter(lambda v:float(v["price"])<=presupuesto, viviendas))
    
    if st.button("Calcular"):
    
        st.table(permitidas)