import sqlite3

class Base_datos:
    def __init__(self):
        self.db = 'database/productos.db'

    def db_consulata(self, query, parametros=()):
        with sqlite3.connect(self.db) as con:
            cursor = con.cursor()
            resultado = cursor.execute(query, parametros)
            con.commit()
        return resultado