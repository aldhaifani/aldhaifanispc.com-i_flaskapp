from flask import Flask, render_template
import os
import base64


def create_app():
    """Creates the flask app

    Return:
        the flask app
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.urandom(24)

    from .views import views

    app.register_blueprint(views, url_prefix="/")

    # database
    user = base64.b64decode(os.environ.get("orders_db_usr").encode("utf-8")).decode(
        "utf-8"
    )
    password = base64.b64decode(
        os.environ.get("orders_db_pass").encode("utf-8")
    ).decode("utf-8")

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{user}:{password}@72.167.207.37/orders"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    return app


application = create_app()


"""

Error Handling

"""


@application.errorhandler(404)
def page_not_found():
    return render_template("404_error.html")


@application.errorhandler(500)
def page_not_found():
    return render_template("500_error.html")
