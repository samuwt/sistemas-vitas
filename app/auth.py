import bcrypt
import psycopg2
from psycopg2.extras import RealDictCursor

# PostgreSQL connection string
DATABASE_URL = "postgresql://postgres:postgres@postgres_db:5432/clinica"

def criar_usuario(email, senha):
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    cursor = conn.cursor()

    # Generate a bcrypt salt and hash the password
    salt = bcrypt.gensalt()
    hashed_senha = bcrypt.hashpw(senha.encode(), salt)

    # Insert the user into the database
    cursor.execute("INSERT INTO usuarios (email, senha) VALUES (%s, %s)", (email, hashed_senha.decode()))
    conn.commit()
    conn.close()

def verificar_usuario(email, senha):
    conn = psycopg2.connect(DATABASE_URL, cursor_factory=RealDictCursor)
    cursor = conn.cursor()
    
    # Fetch the hashed password for the given email
    cursor.execute("SELECT nome, senha FROM usuarios WHERE email = %s", (email,))
    usuario = cursor.fetchone()

    conn.close()
    # nome_usuario = email.split('@')[0]
    # Verify the password using bcrypt
    if usuario and bcrypt.checkpw(senha.encode(), usuario['senha'].encode()):
        return usuario['nome']  # or the appropriate user type
    
    return None