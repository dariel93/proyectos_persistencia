import json

with open("alumnos.json", "r") as f:
    alumnos = json.load(f)
for a in alumnos:
    print(a["nombre"])