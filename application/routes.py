from flask import redirect, url_for, render_template, request
from application import app, db
from application.models import DM, NPC
from application.forms import CreateDM, CreateNPC

@app.route('/')
def home():
    num_DMs = DM.query.count()
    num_NPCs = NPC.query.count()
    dm_list = list(DM.query.all())
    npc_list = list(NPC.query.all())
    dm_npcs = {dm:str([str(npc) for npc in dm.dm_npcs]) for dm in dm_list}
    return render_template('index.html', num = num_DMs, npcs = npc_list, DMs = dm_list, no_NPCs = num_NPCs, dm_npc = dm_npcs)


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

@app.route('/delete/<id>')
def delete():
    return

@app.route('/updatenpc/<int:pk>', methods=['GET', 'POST'])
def updatenpc(pk):
    npc = NPC.query.get(pk)
    dm = DM.query.all()
    Form = CreateNPC()
    Form.dm_id.choices.extend([( dm.dm_id, str(dm)) for dm in dm])
    if request.method == 'POST':
        npc.fk_dm_id = Form.dm_id.data
        npc.npc_name = Form.npc_name.data
        npc.npc_race = Form.npc_race.data
        npc.npc_details = Form.npc_details.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('createNPC.html', form = Form, ptitle = "Update NPC")



# create an entry in a database, uysing keyword as the table 
# field as the field needing entry and its info
@app.route('/createdm', methods=['GET', 'POST'])
def createdm():
    Form = CreateDM()
    if request.method == 'POST':
        forename = Form.forename.data
        surname = Form.surname.data
        new_dm = DM(forename=forename, surname=surname)
        db.session.add(new_dm)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('createDM.html', form = Form)



@app.route('/createnpc', methods=['GET', 'POST'])
def createnpc():
    dm_id = DM.query.all()
    Form = CreateNPC()
    Form.dm_id.choices.extend([( dm.dm_id, str(dm)) for dm in dm_id])
    if request.method == 'POST':
        fk_dm_id = Form.dm_id.data
        npc_name = Form.npc_name.data
        npc_race = Form.npc_race.data
        npc_details = Form.npc_details.data
        new_npc = NPC(fk_dm_id=fk_dm_id, npc_name = npc_name, npc_race = npc_race, npc_details=npc_details)
        db.session.add(new_npc)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('createNPC.html', form = Form)

