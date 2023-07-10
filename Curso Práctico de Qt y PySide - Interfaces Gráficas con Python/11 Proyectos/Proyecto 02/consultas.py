import sys
from path import absPath
from PySide6.QtSql import QSqlDatabase, QSqlQuery


# Crea la conexión
conexion = QSqlDatabase.addDatabase("QSQLITE") 
#para conectar a otra tipo de base de datos, simplemente cambiar el nombre "QSQLITE" - ver en documentation
conexion.setDatabaseName(absPath("clientes.db"))

# print(conexion.databaseName(), conexion.connectionName())
# Abra la conexión
if not conexion.open():
    print("No se puede conectar a la base de datos")
    sys.exit(True)
else:
    print("¿Conexión establecida?", conexion.isOpen())

# # Cree una consulta y ejecútela de inmediato usando .exec ()
consulta = QSqlQuery() #crea la consulta
consulta.exec("DROP TABLE IF EXISTS contactos") #evita duplicados
consulta.exec("""
    CREATE TABLE IF NOT EXISTS contactos (
        id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
        nombre VARCHAR(40) NOT NULL,
        empleo VARCHAR(50),
        email VARCHAR(40) NOT NULL
    )""") #crea la tabla

# print(conexion.tables())

# # Ejecución de consultas dinámicas: formato de cadena
nombre, empleo, email = "Héctor", "Instructor", "hector@ejemplo.com"

consulta.exec(f"""
    INSERT INTO contactos (nombre, empleo, email)
    VALUES ('{nombre}', '{empleo}', '{email}')""")

# # Ejecución de consultas dinámicas: parámetros de marcador de posición
contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

# consulta = QSqlQuery()
consulta.prepare("""
    INSERT INTO contactos (nombre, empleo, email) VALUES (?, ?, ?)""")

# # usamos .addBindValue () para insertar datos
for nombre, empleo, email in contactos:
    consulta.addBindValue(nombre)
    consulta.addBindValue(empleo)
    consulta.addBindValue(email)
    consulta.exec()

# # Consultar registros
consulta.exec("SELECT nombre, empleo, email FROM contactos")

# # ponemos el cursor en el primer registro y sacarlo
if consulta.first():
    print(consulta.value("nombre"),
          consulta.value("empleo"),
          consulta.value("email"))

# # Automatizmaos el cursor hasta el final
while consulta.next():
    print(consulta.value("nombre"),
          consulta.value("empleo"),
          consulta.value("email"))


# # Cerrar conexión a la base de datos
conexion.close()
print("¿Conexión cerrada?", not conexion.isOpen())
