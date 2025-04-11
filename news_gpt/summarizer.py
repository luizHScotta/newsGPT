# news_gpt/summarizer.py

import requests

def resumir_texto(texto, modelo="llama3"):
    """
    Gera um resumo para o texto fornecido usando o modelo especificado via Ollama.

    Parâmetros:
        texto (str): O texto da notícia a ser resumido.
        modelo (str): Nome do modelo a ser usado no Ollama (padrão: 'llama3').

    Retorna:
        str: O resumo gerado.
    """
    url = "http://localhost:11434/api/generate"

    prompt = f"""
    Resuma de forma clara, concisa e informativa o texto abaixo:

    {texto}
    """

    payload = {
        "model": modelo,
        "prompt": prompt,
        "stream": False
    }

    try:
        resposta = requests.post(url, json=payload)
        resposta.raise_for_status()
        return resposta.json()["response"].strip()
    except Exception as e:
        print(f"[ERRO] Falha ao gerar resumo com LLaMA: {e}")
        return "[Erro ao gerar resumo]"


if __name__ == "__main__":
    texto_exemplo = """
    Hackers ligados à Coreia do Norte acumularam bilhões de dólares em criptomoedas após uma série de ciberataques.
    Esse capital tem sido usado para financiar o programa nuclear do país, dizem autoridades.
    """
    resumo = resumir_texto(texto_exemplo)
    print("📝 Resumo:\n", resumo)
