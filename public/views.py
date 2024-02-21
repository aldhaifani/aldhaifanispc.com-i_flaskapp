from flask import Blueprint, render_template, request, flash
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
        print("here")
        result = requests.get(url, timeout=15)
        flash("Order placed successfully! We will  contact you soon.", "success")
    except requests.exceptions.Timeout:
        print("here2")
        flash(
            "Failed to place your order! Please try again or contact us +968-90620008.",
            "danger",
        )
        result = ""

    return result


views = Blueprint("views", __name__)

"""

English routes

"""


@views.route("/en")
@views.route("/en/")
@views.route("/en/home")
@views.route("/en/home/")
def home_en():
    return render_template("home.html", page_link="ar/home", page_lang="en")


@views.route("/en/who_we_are")
@views.route("/en/who_we_are/")
def who_we_are_en():
    return render_template(
        "who_we_are.html", page_link="ar/who_we_are", page_lang="en"
    )


@views.route("/en/how_to_use")
@views.route("/en/how_to_use/")
def how_to_use_en():
    return render_template(
        "how_to_use.html", page_link="ar/how_to_use", page_lang="en"
    )


@views.route("/en/order_now", methods=["GET", "POST"])
@views.route("/en/order_now/", methods=["GET", "POST"])
def order_now_en():
    if request.method == "POST":
        data = request.form
        data_str = ""
        for key in data.keys():
            data_str += key.replace("_", " ").capitalize() + ": "
            data_str += data.get(key) + "\n"
        send_message(data_str)
    return render_template("order_now.html", page_link="ar/order_now", page_lang="en")


@views.route("/en/contact_us")
@views.route("/en/contact_us/")
def contact_us_en():
    return render_template(
        "contact_us.html", page_link="ar/contact_us", page_lang="en"
    )


@views.route("/en/terms_and_conditions")
@views.route("/en/terms_and_conditions/")
def terms_and_conditions_en():
    return render_template(
        "terms_and_conditions.html",
        page_link="ar/terms_and_conditions",
        page_lang="en",
    )


"""

Arabic routes

"""


@views.route("/ar")
@views.route("/ar/")
@views.route("/ar/home")
@views.route("/ar/home/")
def home_ar():
    return render_template("home-rtl.html", page_link="en/home", page_lang="ar")


@views.route("/ar/who_we_are")
@views.route("/ar/who_we_are/")
def who_we_are_ar():
    return render_template(
        "who_we_are-rtl.html", page_link="en/who_we_are", page_lang="ar"
    )


@views.route("/ar/how_to_use")
@views.route("/ar/how_to_use/")
def how_to_use_ar():
    return render_template(
        "how_to_use-rtl.html", page_link="en/how_to_use", page_lang="ar"
    )


@views.route("/ar/order_now", methods=["GET", "POST"])
@views.route("/ar/order_now/", methods=["GET", "POST"])
def order_now_ar():
    if request.method == "POST":
        data = request.form
        data_str = ""
        for key in data.keys():
            data_str += key.replace("_", " ").capitalize() + ": "
            data_str += data.get(key) + "\n"
        send_message(data_str)
    return render_template(
        "order_now-rtl.html", page_link="en/order_now", page_lang="ar"
    )


@views.route("/ar/contact_us")
@views.route("/ar/contact_us/")
def contact_us_ar():
    return render_template(
        "contact_us-rtl.html", page_link="en/contact_us", page_lang="ar"
    )


@views.route("/ar/terms_and_conditions")
@views.route("/ar/terms_and_conditions/")
def terms_and_conditions_ar():
    return render_template(
        "terms_and_conditions-rtl.html",
        page_link="en/terms_and_conditions",
        page_lang="ar",
    )
