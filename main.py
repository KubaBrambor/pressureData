from flask import Flask
from home.home import home
from contact.contact import contact

app = Flask(__name__)
app.register_blueprint(home, url_prefix="/home")
app.register_blueprint(contact, url_prefix="/contact")


if __name__ == '__main__':
    app.run(debug=True)

