from flask import redirect, url_for
from application import app, db
# from application.models import names of databases

@app.route('/')
def home():
    return

# search by table name
# search by some detail from within a table ie; a DM name
# search by a primary key from a table
@app.route('/search/<keyword>')
@app.route('/search/<keyword>/<details>')
@app.route('/search/<keyword>/<id>')
def search():
    return 

@app.route('/delete/<id>')
def delete():
    return

# update by table name, the column, find the ID that needs updating and then the new info
# or correct all entries in a column for general typo's/spelling errors
@app.route('/update/<keyword>/<field>/<id>/<newinfo>')
@app.route('/update/<keyword>/<field>/<oldinfo>/<new info>')
def update():
    return

# create an entry in a database, uysing keyword as the table 
# field as the field needing entry and its info
@app.route('/create/<keyword>/<field>/<info>')
def create():
    return