from flask import Blueprint

views = Blueprint("views", __name__)


@views.route("/en")
@views.route("/en/")
@views.route("/en/home")
@views.route("/en/home/")
def home_en():
    return "english"


@views.route("/ar")
@views.route("/ar/")
@views.route("/ar/home")
@views.route("/ar/home/")
def home_ar():
    return "arabic"
