from flask import Blueprint, render_template

data = Blueprint("data", __name__, static_folder="static", template_folder="templates")

@data.route("/")
def index():
    return render_template("data.html")

