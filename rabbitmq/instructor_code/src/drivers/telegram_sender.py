import requests

def send_telegram_message(message: str) -> None:
    token = "7571124904:AAEyoDMJOpDeHw4RurQUfzFM480J6KQGWss"
    chat_id = -1002371814477

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    requests.post(url, data=payload)
