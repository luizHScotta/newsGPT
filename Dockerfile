# Use uma imagem base oficial do Python com Ubuntu
FROM python:3.12-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie os arquivos de dependências para o contêiner
COPY requirements.txt ./

# Instale as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante do código do projeto
COPY . .

# Comando padrão para executar o aplicativo
CMD ["python", "main.py"]
