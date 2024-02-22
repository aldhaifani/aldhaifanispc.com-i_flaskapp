from flask import flash
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
        flash(
            "Order placed successfully! We will  contact you as soon as possible.",
            "success",
        )
        flash(
            "تم تقديم الطلب بنجاح! سنتواصل معك بأقرب وقت ممكن.",
            "success",
        )
    except requests.exceptions.Timeout:
        flash(
            "Failed to place your order! Please try again or contact us +968-90620008.",
            "danger",
        )
        flash(
            "فشل في تقديم طلبك! يرجى المحاولة مرة أخرى أو الاتصال بنا +968-90620008.",
            "danger",
        )
        result = ""

    return result