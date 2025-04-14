# 🧠 newsGPT

> Um projeto automatizado para buscar, filtrar e enviar por e-mail notícias sobre Inteligência Artificial diariamente.

---

## 🚀 Objetivo

O `newsGPT` é um protótipo que:
1. Busca automaticamente notícias sobre IA nos principais portais (inicialmente G1)
2. Filtra as notícias mais recentes (últimas 24h)
3. (Em breve) resume com IA local usando LLaMA 3
4. Envia por e-mail um resumo com links diariamente

---

## ⚙️ Como rodar localmente com UV (modo dev)

1. Clone o repositório

```bash
git clone https://github.com/luizHScotta/newsGPT.git
cd newsGPT


Crie e ative o ambiente com uv:

uv venv
source .venv/bin/activate
Instale as dependências:

uv pip install -r requirements.txt
Configure seu e-mail no main.py

Execute o projeto:

python main.py

🐳 Como rodar com Docker (modo produção)
⚠️ Nesse modo você não precisa ativar o ambiente virtual.

Construa a imagem:

docker build -t newsgpt .
Rode o projeto:

docker run --rm newsgpt
📬 Envio de e-mail
O projeto usa SMTP para enviar e-mails.
É recomendável gerar uma senha de app (ex: no Gmail com 2FA) e usar um e-mail específico para o envio.

Você pode configurar:

REMETENTE: seu e-mail de envio
SENHA_APP: senha de app (não a senha real)
DESTINATÁRIO: quem vai receber os resumos

🔜 Próximas funcionalidades
✅ Resumo com IA local (LLaMA 3 via Ollama)

✅ Agendamento automático com Prefect

⏳ Adição de outros portais de notícias

📦 Configuração com .env para esconder dados sensíveis

📄 Licença
Este projeto é livre para uso pessoal e educacional.

Feito com 💡 por luizHScotta