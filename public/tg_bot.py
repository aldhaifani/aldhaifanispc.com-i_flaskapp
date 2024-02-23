import os
import requests


# tg_bot message handler
TOKEN = os.environ.get("tg_TOKEN")
chat_id = "360314133"


def send_message(msg):
    url = (
        f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={msg}"
    )

    try:
        result = requests.get(url, timeout=15)
        flash_category = "success"
    except requests.exceptions.Timeout:
        result = ""
        flash_category = "danger"

    return {
        "tg_api_response": result,
        "flash_category": flash_category,
    }
