import mysql.connector 

# Establecer conexión con la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  
    database="rtam",
    port=3306
)

# Verificar conexión
if conexion.is_connected():
    print("✔️ Conexión exitosa a la base de datos")

cursor = conexion.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Cliente (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    tipo VARCHAR(50),
    telefono VARCHAR(20),
    cargo VARCHAR(100)
)
""")


sql = "INSERT INTO Cliente (nombre, tipo, telefono, cargo) VALUES (%s, %s, %s, %s)"

# mis datos aleatorios
datos = [
    ("María López", "Independiente", "3209876543", "Consultora"),
    ("Carlos Gómez", "Empresa", "3145678901", "Jefe de Logística"),
    ("Ana Martínez", "Gobierno", "3123456789", "Directora de Proyectos"),
]

cursor.executemany(sql, datos)

conexion.commit()

print(f"✔️ Se insertaron {cursor.rowcount} registros en la tabla Cliente.")

# Cerrar la conexión
cursor.close()
conexion.close()
