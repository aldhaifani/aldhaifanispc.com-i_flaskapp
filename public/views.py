from .tg_bot import send_message
from flask import Blueprint, render_template, request, flash


import os
import base64
import pymysql.cursors
import datetime
import pytz


views = Blueprint("views", __name__)

"""

Database connection

"""

connection = pymysql.connect(
    host="72.167.207.37",
    user=base64.b64decode(os.environ.get("orders_db_usr").encode("utf-8")).decode(
        "utf-8"
    ),
    password=base64.b64decode(os.environ.get("orders_db_pass").encode("utf-8")).decode(
        "utf-8"
    ),
    database="orders",
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor,
)


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
    return render_template("who_we_are.html", page_link="ar/who_we_are", page_lang="en")


@views.route("/en/how_to_use")
@views.route("/en/how_to_use/")
def how_to_use_en():
    return render_template("how_to_use.html", page_link="ar/how_to_use", page_lang="en")


@views.route("/en/order_now", methods=["GET", "POST"])
@views.route("/en/order_now/", methods=["GET", "POST"])
def order_now_en():
    lastorder_id = 0
    if request.method == "POST":
        data = request.form

        data_str = ""
        for key in data.keys():
            data_str += key.replace("_", " ").capitalize() + ": "
            data_str += data.get(key) + "\n"

        send_message_data = send_message(data_str)
        flash("", send_message_data["flash_category"])

        if send_message_data.get("flash_category") == "success":

            with connection.cursor() as cursor:
                # Create a new record
                date_today = datetime.datetime.now(pytz.timezone("Asia/Muscat"))
                sql = "INSERT INTO `orders_tbl`(`date`, `order_qty`, `customer_name`, `phone_number`, `email`,`location`, `completed`) VALUES ({},{},{},{},{},{},{})".format(
                    date_today.strftime("%b %d, %Y"),
                    data.get("total_qty"),
                    data.get("full_name"),
                    data.get("phone_number"),
                    data.get("email"),
                    f"{data.get('country')}, {data.get('city')}, {data.get('area')}, {data.get('street')}, Bld {data.get('house_number')}",
                    0,
                )
                cursor.execute(sql)

            lastorder_id = f"#{date_today.strftime('%Y%m')}{connection.insert_id()}"
            connection.commit()

            data_str += lastorder_id + "\n"

    return render_template(
        "order_now.html",
        page_link="ar/order_now",
        page_lang="en",
        order_id=lastorder_id,
    )


@views.route("/en/contact_us")
@views.route("/en/contact_us/")
def contact_us_en():
    return render_template("contact_us.html", page_link="ar/contact_us", page_lang="en")


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

        send_message_data = send_message(data_str)
        flash("flash_msg", send_message_data["flash_category"])

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
