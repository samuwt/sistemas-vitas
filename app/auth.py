import bcrypt
import sqlite3
def criar_usuario(email, senha):
    conn = sqlite3.connect('clinica.db')
    cursor = conn.cursor()
    
    # Generate a bcrypt salt and hash the password
    salt = bcrypt.gensalt()
    hashed_senha = bcrypt.hashpw(senha.encode(), salt)
    
    cursor.execute("INSERT INTO usuarios (email, senha) VALUES (?, ?)", (email, hashed_senha.decode()))
    conn.commit()
    conn.close()
    
def verificar_usuario(email, senha):
    conn = sqlite3.connect('clinica.db')
    cursor = conn.cursor()
    
    cursor.execute("SELECT senha FROM usuarios WHERE email = ?", (email,))
    usuario = cursor.fetchone()
    
    conn.close()
    
    if usuario and bcrypt.checkpw(senha.encode(), usuario[0].encode()):
        return "medico"  # or the appropriate user type
    
    return None