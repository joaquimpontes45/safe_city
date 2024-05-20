import sqlite3
import os

def conectar():
    if not os.path.exists('database'):
        os.makedirs('database')
    if not os.path.exists('database/sqlite.db'):
        conn = sqlite3.connect('database/sqlite.db')
        create_tables(conn)
    else:
        conn = sqlite3.connect('database/sqlite.db')
        create_tables(conn)
    conn.row_factory = sqlite3.Row
    return conn
def create_tables(conn):
    conn.execute('''
        CREATE TABLE IF NOT EXISTS denuncias(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Nome VARCHAR NOT NULL,
            telefone VARCHAR,
            cidade TEXT NOT NULL,
            bairro TEXT NOT NULL,
            rua TEXT NOT NULL,
            tipo_do_crime VARCHAR NOT NULL,
            data DATE NOT NULL,
            hora TIME NOT NULL,
            cor_criminoso TEXT NOT NULL,
            sexo VARCHAR NOT NULL,
            Altura VARCHAR NOT NULL,
            descricao TEXT NOT NULL
        )
    ''')
