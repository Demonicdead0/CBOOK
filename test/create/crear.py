import sqlite3
import os

print(os.getcwd())

# crear archivo con extensión .cbook
conn = sqlite3.connect("mis_datos.cbook")
cursor = conn.cursor()

with open("codigo.sql", "r", encoding="utf-8") as archivo_sql:
    script = archivo_sql.read()

cursor.execute(script)

conn.commit()
conn.close()
print("Base de dato mis_datos.cbook creada correctamente")