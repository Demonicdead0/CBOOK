import os
import sqlite3

class Cbook:
    def __init__(self, ruta_carpeta):
        self.ruta = ruta_carpeta
    
    def crear(self):
        conn = sqlite3.connect(self.ruta)
        cursor = conn.cursor()
        with open("script.sql", "r", encoding="utf-8") as sql:
            script = sql.read()
        cursor.execute(script)

        conn.commit()
        conn.close()
        print(f"Base de datos {self.ruta} creado con exito")

    def agregar(self, nombre_db, ruta,nombre_archivo,ruta_real):
        conn = sqlite3.connect(nombre_db)
        cursor = conn.cursor()

        with open(ruta_real, "rb") as f:
            contenido = f.read()
        cursor.execute("INSERT INTO cbook (ruta, nombre, contenido) VALUES (?,?,?)", (ruta, nombre_archivo,contenido))
        conn.commit()
        conn.close()
        print(f"Archivo {nombre_db} actualizado con exito")

        # ejemplos
        # agregar_archivo("mis_datos.dadada", "docs/", "manual.txt", "manual.txt")
        # agregar_archivo("mis_datos.dadada", "imagenes/", "foto.jpg", "foto.jpg")
        # agregar_archivo("mis_datos.dadada", "imagenes/eventos/", "evento.png", "evento.png")
    
    def recuperar(self, nombre_db, ruta, nombre_archivo, ruta_salida):
        conn = sqlite3.connect(nombre_db)
        cursor = conn.cursor()

        cursor.execute("SELECT contenido FROM cbook WHERE ruta = ? AND nombre = ?", (ruta, nombre_archivo))
                
