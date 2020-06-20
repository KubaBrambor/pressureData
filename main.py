from flask import Flask
from index.second import second
from contact.contact import contact
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.register_blueprint(second, url_prefix="")
app.register_blueprint(contact, url_prefix="/contact")


if __name__ == '__main__':
    app.run(debug=True)

