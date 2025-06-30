import requests


def send_telegram_message(message: str) -> None:
    token = "7645749359:AAEhImRTl6VYeBEaGrZkBhpuRq1v2govcgs"
    chat_id = -4935999269

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": message
    }

    requests.post(url, data=payload)
