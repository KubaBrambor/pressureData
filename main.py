from flask import Flask
from index.second import second
from contact.contact import contact

app = Flask(__name__)
app.register_blueprint(second, url_prefix="")
app.register_blueprint(contact, url_prefix="/contact")


if __name__ == '__main__':
    app.run(debug=True)

