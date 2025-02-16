CREATE TABLE IF not exists cbook(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ruta TEXT, -- Ruta dentro del "archivo-carpeta"
    nombre TEXT,
    contenido BLOB
)