import sqlite3
import os

DB_NAME = 'clinica.db'

# Obtém o caminho absoluto do diretório do arquivo atual
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SQL_FILE = os.path.join(BASE_DIR, 'init_db.sql')  # Caminho correto para init_db.sql

def conectar():
    conn = sqlite3.connect(DB_NAME)
    return conn

def criar_tabelas():
    conn = conectar()
    with open(SQL_FILE, "r") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

if __name__ == "__main__":
    criar_tabelas()