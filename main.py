# main.py

from news_gpt.scraper import buscar_noticias_g1
from news_gpt.notifier import enviar_email

# Configurações
REMETENTE = "seuemail@gmail.com"
SENHA_APP = "sua_senha_de_app_aqui"
DESTINATARIO = "luizhgscotta@gmail.com"

def montar_resumos_sem_ia(noticias):
    return [
        {
            "titulo": n["titulo"],
            "link": n["link"],
            "resumo": "⚠️ Resumo ainda não gerado com IA."
        }
        for n in noticias
    ]

def main():
    print("🔍 Buscando notícias...")
    noticias = buscar_noticias_g1()

    if not noticias:
        print("⚠️ Nenhuma notícia encontrada.")
        return

    print(f"✉️ {len(noticias)} notícia(s) encontrada(s). Enviando e-mail...")

    resumos = montar_resumos_sem_ia(noticias)
    enviar_email(resumos, REMETENTE, SENHA_APP, DESTINATARIO)

if __name__ == "__main__":
    main()
