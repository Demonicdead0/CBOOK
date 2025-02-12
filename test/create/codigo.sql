CREATE TABLE IF not exists archivo(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT UNIQUE,
    contenido BLOB
)