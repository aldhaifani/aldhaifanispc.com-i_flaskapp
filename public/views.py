from flask import Blueprint

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
@views.route("/home/")
def redirect_lang():
    return "Hello World!"
