from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import pymysql
from os import getenv

app = Flask(__name__)
#] app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dnd.db'
# mysql+pymysql://<root username>:<root password>@<zip address>:3306/flask_demo_db where flask_demo_db is the name of the db in the virtual SQL instance
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('db_uri')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = getenv('secret_key')

db = SQLAlchemy(app)

import application.routes