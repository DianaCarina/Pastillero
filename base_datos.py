import sqlite3

# Crar la conexion
miConexion = sqlite3.connect("Pastillero")
# Crar el cursor
miCursor = miConexion.cursor()

# Dar las insrucciones a SQL
miCursor.execute("CREATE TABLE PASTILLERO(ID_PX INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_PX VARCHAR(20), EDAD INTEGER, DX VARCHAR(50), NUMERO_MEDICAMENTOS INTEGER)")

# Confirmar cambios y cerrar BD
miConexion.commit()
miConexion.close()