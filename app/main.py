from flask import Flask, request, jsonify, session, redirect
from auth import verificar_usuario
from db import criar_tabelas

app = Flask(__name__)
app.secret_key = 'chave_secreta'

setup_done = False

@app.before_request
def setup():
    global setup_done
    if not setup_done:
        criar_tabelas()
        setup_done = True

@app.route('/')
def home():
    return "API Rodando!"

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    senha = data.get('senha')
    
    tipo_usuario = verificar_usuario(email, senha)
    
    if tipo_usuario:
        session['usuario'] = email
        session['tipo'] = tipo_usuario
        return jsonify({"message": f"Bem-vindo, {tipo_usuario}!"}), 200
    
    return jsonify({"error": "Credenciais inválidas"}), 401

@app.route('/logout')
def logout():
    session.clear()
    return jsonify({"message": "Logout realizado"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)