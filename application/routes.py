from flask import redirect, url_for, render_template, request
from application import app, db, player_character
from application.models import DM, NPC, Player, Player_character
from application.forms import CreateDM, CreateNPC, CreatePlayer


@app.route('/')
def home():
    num_DMs = DM.query.count()
    num_NPCs = NPC.query.count()
    dm_list = list(DM.query.all())
    npc_list = list(NPC.query.all())
    player_list = list(Player.query.all())
    num_players = Player.query.count()
    num_characters = Player_character.query.count()
    character_list = list(Player_character.query.all())
    return render_template('index.html', ptitle = 'Home Page' ,num = num_DMs, npcs = npc_list, \
        DMs = dm_list, no_NPCs = num_NPCs, players = player_list, no_players = num_players,\
            no_characters=num_characters, characters=character_list )


# Below is the CRUD functionality associated to the DM table
@app.route('/deletedm/<int:pk>')
def deletedm(pk):
    todelete = DM.query.get(pk)
    db.session.delete(todelete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/searchnpc/int:<pk>')
def searchnpc(pk):
    dm = DM.query.get(pk)
    dm_npcs = dm.dm_npcs
    return render_template('DMsearch.html',list = dm_npcs, ptitle = "List of DM associated NPCs")

@app.route('/updatedm/<int:pk>', methods=['POST', 'GET'])
def updatedm(pk):
    dm = DM.query.get(pk)
    Form = CreateDM()
    if request.method == 'POST':
        dm.forename = Form.forename.data
        dm.surname = Form.surname.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('createDM.html', form = Form, ptitle = 'Update DM')

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
    return render_template('createDM.html', form = Form, ptitle = 'Create DM')




# Below is the CRUD functionality for the NPC table

@app.route('/deletenpc/<int:pk>')
def deletenpc(pk):
    todelete = NPC.query.get(pk)
    db.session.delete(todelete)
    db.session.commit()
    return redirect(url_for('home'))

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
    return render_template('createNPC.html', form = Form, ptitle = 'Create new NPC')




# Below is the CRUD functionality for the player table

@app.route('/createplayer', methods=['GET', 'POST'])
def createplayer():
    dm_id = DM.query.all()
    Form = CreatePlayer()
    Form.dm_id.choices.extend([( dm.dm_id, str(dm)) for dm in dm_id])
    if request.method == 'POST':
        fk_dm_id = Form.dm_id.data
        forename = Form.forename.data
        surname = Form.surname.data
        new_player = Player(fk_dm_id = fk_dm_id, forename = forename, surname = surname)
        db.session.add(new_player)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('createPlayer.html', form = Form, ptitle = 'Create new Player')


@app.route('/updateplayer/<int:pk>', methods=['GET', 'POST'])
def updateplayer(pk):
    player = Player.query.get(pk)
    dm = DM.query.all()
    Form = CreatePlayer()
    Form.dm_id.choices.extend([( dm.dm_id, str(dm)) for dm in dm])
    if request.method == 'POST':
        player.fk_dm_id = Form.dm_id.data
        player.forename = Form.forename.data
        player.surname = Form.surname.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('createPlayer.html', form = Form, ptitle = "Update Player")

@app.route('/deleteplayer/<int:pk>')
def deleteplayer(pk):
    todelete = Player.query.get(pk)
    db.session.delete(todelete)
    db.session.commit()
    return redirect(url_for('home'))

