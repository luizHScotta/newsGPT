# news_gpt/scraper.py

import re
import requests
import urllib3
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# Desativa aviso de certificado SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Palavras-chave para filtrar notícias relacionadas a IA
PALAVRAS_CHAVE = [
    r"\binteligência artificial\b",
    r"\bia\b",
    r"\bmachine learning\b",
    r"\baprendizado de máquina\b",
    r"\bhackers\b"
]

def interpretar_data_humanizada(texto):
    """Converte textos como 'Há 3 horas' em um datetime real."""
    texto = texto.strip().lower()
    agora = datetime.now()

    if "há" in texto:
        if "minuto" in texto:
            minutos = int(re.search(r"\d+", texto).group())
            return agora - timedelta(minutes=minutos)
        elif "hora" in texto:
            horas = int(re.search(r"\d+", texto).group())
            return agora - timedelta(hours=horas)
        elif "ontem" in texto:
            return agora - timedelta(days=1)
    return None  # Não conseguiu interpretar

def buscar_noticias_g1():
    """Busca notícias de IA publicadas nas últimas 24h no G1 Tecnologia."""
    url = "https://g1.globo.com/tecnologia/"
    response = requests.get(url, verify=False)
    soup = BeautifulSoup(response.text, "html.parser")

    noticias = []
    agora = datetime.now()
    limite = agora - timedelta(hours=24)

    for item in soup.select("div.feed-post-body"):
        link_tag = item.select_one("a.feed-post-link")
        data_span = item.select_one("span.feed-post-datetime")

        if not link_tag or not data_span:
            continue

        titulo = link_tag.text.strip()
        texto = titulo.lower()

        if not any(re.search(padrao, texto) for padrao in PALAVRAS_CHAVE):
            continue

        data_publicacao = interpretar_data_humanizada(data_span.text)
        if not data_publicacao or data_publicacao < limite:
            continue

        noticias.append({
            "fonte": "G1",
            "titulo": titulo,
            "link": link_tag["href"],
            "data": data_publicacao.isoformat()
        })

    return noticias

# Teste local do scraper
if __name__ == "__main__":
    noticias = buscar_noticias_g1()
    print(f"🔍 {len(noticias)} notícia(s) encontrada(s) nas últimas 24h:\n")
    for n in noticias:
        print(f"[{n['data']}] {n['titulo']} ({n['fonte']})\n→ {n['link']}\n")
