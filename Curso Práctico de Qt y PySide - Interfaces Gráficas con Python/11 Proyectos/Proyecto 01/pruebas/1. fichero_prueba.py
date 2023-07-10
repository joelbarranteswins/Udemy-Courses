import json
from helpers import absPath

# Creamos la estructura de datos
datos = []

# Añadimos un registro manualmente
datos.append({
    "nombre": "Héctor",
    "empleo": "Instructor",
    "email": "hector@ejemplo.com"
})

# Definimos una lista de contactos
contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

#nombre, empleo, email
# Añadimos un contactos dinámicamente
for a, b ,c in contactos:
    datos.append({
        "nombre": a,
        "empleo": b,
        "email": c
    })

# Guardamos los registros del fichero
with open(absPath("clientes.json"), "w") as fichero:
    json.dump(datos, fichero)

# # Leemos los registros del fichero
with open(absPath("clientes.json")) as fichero:
    datos = json.load(fichero)
    for contacto in datos:
        print(contacto['nombre'], contacto['empleo'], contacto['email'])
