import mysql.connector

def conectar():
    """Establece conexión con la base de datos."""
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="rtam",
            port=3306
        )
        if conexion.is_connected():
            print("✔️ Conexión exitosa a la base de datos")
        return conexion
    except mysql.connector.Error as e:
        print(f"❌ Error al conectar a la base de datos: {e}")
        return None

if __name__ == "__main__":
    conectar() 

#INSERTAR LOS DATOS DE LAS PERSONAS
def insertar_clientes():
    conexion = conectar()
    if not conexion:
        return
    try:
        cursor = conexion.cursor()
        sql = "INSERT INTO Cliente (nombre, tipo, telefono, cargo) VALUES (%s, %s, %s, %s)"
        datos = [
            ("Juan Pérez", "Empresa", "3112345678", "Gerente de Compras"),
            ("María López", "Independiente", "3209876543", "Consultora"),
            ("Carlos Gómez", "Empresa", "3145678901", "Jefe de Logística"),
            ("Ana Martínez", "Gobierno", "3123456789", "Directora de Proyectos"),
            ("Luis Ramírez", "Empresa", "3156789012", "Coordinador de Ventas"),
        ]
        cursor.executemany(sql, datos)
        conexion.commit()
        print(f"✔️ Se insertaron {cursor.rowcount} registros en la tabla Cliente.")
    except mysql.connector.Error as err:
        print(f"❌ Error al insertar clientes: {err}")
    finally:
        cursor.close()
        conexion.close()

#CONSULTAR DATOS
def consultar_clientes(id_cliente=None):
    conexion = conectar()
    if not conexion:
        return
    try:
        cursor = conexion.cursor()
        if id_cliente:
            cursor.execute("SELECT * FROM Cliente WHERE id = %s", (id_cliente,))
        else:
            cursor.execute("SELECT * FROM Cliente")
        clientes = cursor.fetchall()
        if clientes:
            print("📋 Lista de clientes:")
            for cliente in clientes:
                print(cliente)
        else:
            print("⚠️ No hay clientes registrados o no se encontró el cliente.")
    except mysql.connector.Error as err:
        print(f"❌ Error al consultar clientes: {err}")
    finally:
        cursor.close()
        conexion.close()

#ACTUALIZAR DATOS
def actualizar_cliente(id_cliente, nuevo_nombre, nuevo_tipo, nuevo_telefono, nuevo_cargo):
    conexion = conectar()
    if not conexion:
        return
    try:
        cursor = conexion.cursor()
        sql = "UPDATE Cliente SET nombre = %s, tipo = %s, telefono = %s, cargo = %s WHERE id = %s"
        cursor.execute(sql, (nuevo_nombre, nuevo_tipo, nuevo_telefono, nuevo_cargo, id_cliente))
        conexion.commit()
        if cursor.rowcount > 0:
            print(f"✔️ Cliente con ID {id_cliente} actualizado correctamente.")
        else:
            print(f"⚠️ No se encontró un cliente con ID {id_cliente}.")
    except mysql.connector.Error as err:
        print(f"❌ Error al actualizar cliente: {err}")
    finally:
        cursor.close()
        conexion.close()

#ELIMINAR DATOS
def eliminar_cliente(id_cliente):
    """Elimina un cliente de la base de datos por su ID"""
    conexion = conectar()
    if not conexion:
        return
    try:
        cursor = conexion.cursor()
        sql = "DELETE FROM Cliente WHERE id = %s"
        cursor.execute(sql, (id_cliente,))
        conexion.commit()
        if cursor.rowcount > 0:
            print(f"✔️ Cliente con ID {id_cliente} eliminado correctamente.")
        else:
            print(f"⚠️ No se encontró un cliente con ID {id_cliente}.")
    except mysql.connector.Error as err:
        print(f"❌ Error al eliminar cliente: {err}")
    finally:
        cursor.close()
        conexion.close()

# Ejecución de funciones
if __name__ == "__main__":
    insertar_clientes()
    consultar_clientes()
    actualizar_cliente()
    eliminar_cliente() 
    consultar_clientes()
