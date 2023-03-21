# Define a imagem base
FROM python:3.10

# Copia o codigo do projeto para dentro do contêiner
COPY . /app

# Define o diretorio de trabalho
WORKDIR /app

# Instala as dependencias do projeto
RUN pip install -r requirements.txt

# Expoe a porta 8000
EXPOSE 8000

# Define o comando para iniciar o servidor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]