from flask import Blueprint, render_template

contact = Blueprint("contact", __name__, static_folder="static", template_folder="templates")

@contact.route('/')
def main():
    return render_template('contact.html')