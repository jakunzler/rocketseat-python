import json
import os
from src.drivers.telegram_sender import send_telegram_message


def rabbitmq_callback(channel, method, properties, body):
    msg_bytes = body.decode("utf-8")
    msg = json.loads(msg_bytes)
    print(msg)
    print(msg["msg"])
    
    send_telegram_message(os.getenv("TG_CHAT_ID"), msg["msg"])

