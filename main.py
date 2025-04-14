# main.py

from news_gpt.scraper.g1 import buscar_noticias_g1
from news_gpt.scraper.tecmundo import buscar_noticias_tecmundo
from news_gpt.notifier import enviar_email

# Configurações
REMETENTE = "luizhgscotta@gmail.com"
SENHA_APP = "pojounfwlbsjelvr"
DESTINATARIO = "lhscotta@hotmail.com"

from news_gpt.summarizer import resumir_texto

def montar_resumos_com_ia(noticias):
    resumos = []
    for noticia in noticias:
        print(f"🧠 Resumindo: {noticia['titulo']}")
        resumo = resumir_texto(noticia["titulo"])
        resumos.append({**noticia, "resumo": resumo})
    return resumos


def main():
    print("🔍 Buscando notícias...")
    noticias = buscar_noticias_g1() + buscar_noticias_tecmundo()

    if not noticias:
        print("⚠️ Nenhuma notícia encontrada.")
        return

    print(f"✉️ {len(noticias)} notícia(s) encontrada(s). Enviando e-mail...")

    resumos = montar_resumos_com_ia(noticias)
    enviar_email(resumos, REMETENTE, SENHA_APP, DESTINATARIO)

if __name__ == "__main__":
    main()
