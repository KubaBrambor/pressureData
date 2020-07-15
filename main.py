import os, datetime
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import Column, Integer, DateTime
from flask import Flask, render_template
from data.data import data
from contact.contact import contact

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.register_blueprint(data, url_prefix="/data")
app.register_blueprint(contact, url_prefix="/contact")
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    pressures = db.relationship('Pressure', backref='user')

    def __repr__(self):
        return f'<User {self.username}>'

class Pressure(db.Model):
    __tablename__ = 'pressure'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    created_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Pressure {self.amount}>'

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Pressure=Pressure)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

