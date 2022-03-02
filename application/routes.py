from flask import redirect, url_for, render_template
from application import app, db
from application.models import DM

@app.route('/')
def home():
    num_DMs = DM.query.count()
    dm_list = [str(dm) for dm in DM.query.all()]
    #dm_list = [str(DM) + " " + str(todo.project) for todo in Todo.query.all()]
    return render_template('index.html', num = num_DMs, DMs = dm_list)
    
    # and then in html - {{ to do }} in side a {% for %} {% end for %}

# search by table name
# search by some detail from within a table ie; a DM name
# search by a primary key from a table
@app.route('/searchdm')
@app.route('/searchdm/<field>')
@app.route('/searchdm/<details>')
@app.route('/searchdm/<id>')
# come back to refactor, remove duplicated code
def searchdm(details=None,field=None, id=None):
    if not details and not id:
        data = db.session.execute(f"SELECT * FROM dm")
        result = list('<br>'.join([str(res) for res in data]))
        length_check = len(result)
        return render_template('search.html', output = result, length = length_check)
    elif details and not id:
        data = db.session.execute(f"SELECT * FROM dm WHERE {field} LIKE '%{details}%'")
        result = list('<br>'.join([str(res) for res in data]))
        length_check = len(result)
        return render_template('search.html', output = result, length = length_check)
    elif field and not details and not id:
        data = db.session.execute(f"SELECT {field} FROM dm")
        result = list('<br>'.join([str(res) for res in data]))
        length_check = len(result)
        return render_template('search.html', output = result, length = length_check)
    elif id:
        data = db.session.execute(f"SELECT * FROM dm WHERE dm_id={id}")
        result = list('<br>'.join([str(res) for res in data]))
        length_check = len(result)
        return render_template('search.html', output = result, length = length_check)
<<<<<<< HEAD
=======
    return 
>>>>>>> db19abcb579bd4d6b4e0c72038c12c30d5a51087

@app.route('/delete/<id>')
def delete():
    return

# update by table name, the column, find the ID that needs updating and then the new info
# or correct all entries in a column for general typo's/spelling errors
@app.route('/update/<keyword>/<field>/<id>/<newinfo>')
@app.route('/update/<keyword>/<field>/<oldinfo>/<newinfo>')
def update():
    return

# create an entry in a database, uysing keyword as the table 
# field as the field needing entry and its info
@app.route('/createdm/<forename>')
@app.route('/createdm/<forename>/<surname>')
@app.route('/createdm/<forename>/<surname>/<npc_id>')
@app.route('/createdm/<forename>/<surname>/<npc_id>/<player_id>')
def createdm(forename = "", surname = "", npc_id = None, player_id = None):
    if player_id == None and npc_id == None:
        new_dm = DM(forename = forename, surname = surname)
    elif player_id == None:
        new_dm = DM(forename = forename, surname = surname, npc_id = npc_id)
    else:
        new_dm = DM(forename = forename, surname = surname, npc_id = npc_id, player_id = player_id)
    db.session.add(new_dm)
    db.session.commit()
    return render_template('create.html', name = forename)