# news_gpt/scraper/tecmundo.py

import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

PALAVRAS_CHAVE = [
     r"\binteligência artificial\b",
    r"\bia\b",
    r"\bmachine learning\b",
    r"\baprendizado de máquina\b",
    r"\bhackers\b",
    r"\bmusk\b",
    r"\btrump\b"
]

def buscar_noticias_tecmundo():
    url = "https://www.tecmundo.com.br/novidades"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    noticias = []
    agora = datetime.now()
    limite = agora - timedelta(hours=24)

    for card in soup.select("article.tec--card"):
        link_tag = card.select_one("a.tec--card__title__link")
        data_tag = card.select_one("div.tec--timestamp__item")

        if not link_tag or not data_tag:
            continue

        titulo = link_tag.text.strip()
        link = link_tag["href"]
        data_br = data_tag.text.strip()

        try:
            data_publicacao = datetime.strptime(data_br, "%d/%m/%Y")
        except:
            data_publicacao = agora  # fallback

        texto = titulo.lower()
        if not any(re.search(p, texto) for p in PALAVRAS_CHAVE):
            continue

        # filtra por notícias nas últimas 24 horas
        if data_publicacao >= limite:
            noticias.append({
                "fonte": "TecMundo",
                "titulo": titulo,
                "link": link,
                "data": data_publicacao.isoformat()
            })

    return noticias

# Teste local
if __name__ == "__main__":
    noticias = buscar_noticias_tecmundo()
    print(f"🔍 {len(noticias)} notícia(s) encontradas no TecMundo:\n")
    for n in noticias:
        print(f"[{n['data']}] {n['titulo']} ({n['fonte']})\n→ {n['link']}\n")
