import json, csv
    
with open("countries.json", "r" , encoding="utf-8") as file:
    data = json.load(file)
    
capitales = list(set(map(lambda c: c["region"], data)))   
print(capitales)

with open("empleados.csv", "r", encoding="utf-8") as f:
    empleados = csv.DictReader(f)
    
    nombres = [empleado["empleado"] for empleado in empleados]
    print(nombres)
    
with open("dias.txt" , "r" , encoding="utf-8") as f:
    data = f.readlines()
    dias = list(map(lambda d: d.strip(), data))
    print(dias)
    


