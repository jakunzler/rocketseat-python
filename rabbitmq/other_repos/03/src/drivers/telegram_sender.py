import os

import requests
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

# Obtém os valores das variáveis de ambiente
BOT_TOKEN = os.getenv("BOT_TOKEN")
BOT_GROUP_CHAT_ID = os.getenv("BOT_GROUP_CHAT_ID")


def send_telegram_message(message: str) -> None:

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": {BOT_GROUP_CHAT_ID},
        "text": message,
        "parse_mode":  "MarkdownV2"
    }
    response = requests.post(url, data=payload, timeout=10)

    # Verifica erros na resposta da API
    if response.status_code != 200:
        print("Erro ao enviar mensagem:", response.text)
