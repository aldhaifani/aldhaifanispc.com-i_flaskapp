from flask import Blueprint, render_template

views = Blueprint("views", __name__)

"""

English routes

"""


@views.route("/en")
@views.route("/en/")
@views.route("/en/home")
@views.route("/en/home/")
def home_en():
    return render_template("home.html")


"""

Arabic routes

"""


@views.route("/ar")
@views.route("/ar/")
@views.route("/ar/home")
@views.route("/ar/home/")
def home_ar():
    return "arabic"
