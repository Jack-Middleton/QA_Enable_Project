from flask import redirect, url_for, render_template, request
from application import app, db, player_character
from application.models import DM, NPC, Player, Player_character, Equipment, Spells
from application.forms import CreateDM, CreateNPC, CreatePlayer, CreateEquipment, CreateSpell


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
    num_equipment = Equipment.query.count()
    equipment_list = list(Equipment.query.all())
    num_spells = Spells.query.count()
    spell_list = list(Spells.query.all())
    return render_template('index.html', ptitle = 'Home Page' ,num = num_DMs, npcs = npc_list, \
        DMs = dm_list, no_NPCs = num_NPCs, players = player_list, no_players = num_players,\
            no_characters=num_characters, characters=character_list, no_equipment=num_equipment, equipment=equipment_list, \
            no_spells = num_spells, spells = spell_list )


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

# Below is the CRUD functionality for the Equipment table

@app.route('/createEquipment', methods=['GET', 'POST'])
def createEquipment():
    character_id = Player_character.query.all()
    Form = CreateEquipment()
    Form.pc_id.choices.extend([(character.pc_id, str(character)) for character in character_id])
    if request.method == 'POST':
        fk_pc_id = Form.pc_id.data 
        equipment_name = Form.equipment_name.data
        equipment_details = Form.equipment_details.data 
        is_weapon = Form.is_weapon.data
        str_dex = Form.str_dex.data  
        distance = Form.distance.data 
        dice_type = Form.dice_type.data
        rarity = Form.rarity.data
        new_equipment = Equipment(fk_pc_id=fk_pc_id, equipment_name=equipment_name, \
            equipment_details=equipment_details, is_weapon=is_weapon, str_dex=str_dex, distance=distance, \
            dice_type=dice_type, rarity=rarity)
        db.session.add(new_equipment)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('createEquipment.html', form=Form, ptitle='Create new Equipment')

@app.route('/deleteEquipment/<int:pk>')
def deleteEquipment(pk):
    todelete = Equipment.query.get(pk)
    db.session.delete(todelete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/updateEquipment/<int:pk>', methods=['GET','POST'])
def updateEquipment(pk):
    equipment = Equipment.query.get(pk)
    character_id = Player_character.query.all()
    Form = CreateEquipment()
    Form.pc_id.choices.extend([(character.pc_id, str(character)) for character in character_id])
    if request.method == 'POST':
        equipment.fk_pc_id = Form.pc_id.data 
        equipment.equipment_name = Form.equipment_name.data
        equipment.equipment_details = Form.equipment_details.data 
        equipment.is_weapon = Form.is_weapon.data
        equipment.str_dex = Form.str_dex.data  
        equipment.distance = Form.distance.data 
        equipment.dice_type = Form.dice_type.data
        equipment.rarity = Form.rarity.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('createEquipment.html', form=Form, ptitle=f"Update {equipment.equipment_name}")


# Below is CRUD functionality for Spells table 

@app.route('/createspell', methods=['GET', 'POST'])
def createspell():
    character_id = Player_character.query.all()
    Form = CreateSpell()
    Form.pc_id.choices.extend([(character.pc_id, str(character)) for character in character_id])
    if request.method == 'POST':
        fk_pc_id = Form.pc_id.data
        spell_name = Form.spell_name.data
        spell_details = Form.spell_details.data
        spell_level = Form.spell_level.data
        new_spell = Spells(fk_pc_id=fk_pc_id, spell_name=spell_name, spell_details=spell_details, spell_level=spell_level)
        db.session.add(new_spell)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('createSpell.html', form = Form, ptitle = 'Create new Spell')


@app.route('/deletespell/<int:pk>')
def deletespell(pk):
    todelete = Spells.query.get(pk)
    db.session.delete(todelete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/updatespell/<int:pk>')
def updatespell(pk):
    spell = Spells.query.get(pk)
    character_id = Player_character.query.all()
    Form = CreateSpell()
    Form.pc_id.choices.extend([(character.pc_id, str(character)) for character in character_id])
    if request.method == 'POST':
        spell.fk_pc_id = Form.pc_id.data
        spell.spell_name = Form.spell_name.data
        spell.spell_details = Form.spell_details.data
        spell.spell_level = Form.spell_level.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('createSpell.html', form=Form, ptitle=f'Update {spell.spell_name}')