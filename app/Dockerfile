# Usando uma imagem base do Python
FROM python:3.9

# Definindo o diretório de trabalho dentro do container
WORKDIR /app

# Copiar todos os arquivos do diretório raiz para dentro do container
COPY . /app

# Instalando as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Expondo a porta da aplicação
EXPOSE 5000

# Comando para rodar a aplicação
#CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
CMD ["python", "main.py"]
