# news_gpt/mailer.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(resumos, remetente, senha_app, destinatario):
    msg = MIMEMultipart()
    msg['From'] = remetente
    msg['To'] = destinatario
    msg['Subject'] = "Resumo diário de notícias sobre IA 🧠🗞️"

    corpo = "<h2>🧠 Notícias sobre IA (últimas 24h)</h2><ul>"

    for n in resumos:
        corpo += f"""
        <li>
            <strong>{n['titulo']}</strong><br>
            <a href="{n['link']}">Leia a notícia</a><br>
            <p>{n['resumo']}</p>
        </li><br>
        """

    corpo += "</ul>"

    msg.attach(MIMEText(corpo, 'html'))

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(remetente, senha_app)
            server.send_message(msg)
        print("✅ E-mail enviado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")
