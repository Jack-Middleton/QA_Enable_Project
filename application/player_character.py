# I'm moving all functionality for the player_character into here to add readability
# Because there needs to be several calcs to determine outputs
# so putting that all into the routes file felt like it would create a bit of a mess


from flask import redirect, url_for, render_template, request
from application import app, db
from application.models import DM, NPC, Player, Player_character, Equipment
from application.forms import CreateDM, CreateNPC, CreatePlayer, CreatePlayerCharacter
from math import ceil

@app.route('/displaycharacter/<int:pk>')
def displaycharacter(pk):
    character = Player_character.query.get(pk)
    foreign_key = int(character.fk_player_id)
    player = Player.query.get(foreign_key)
    equipment = character.pc_equipment
    # to determine stats for later, a proficiency bonus is needed using the level
    proficiency = 0
    if character.level <= 4:
        proficiency = 2
    elif character.level <= 8:
        proficiency = 3
    elif character.level <= 12:
        proficiency = 4
    elif character.level <= 16:
        proficiency = 5
    else:
        proficiency = 5
    # depending on the race, some of those stats gain a racial bonus, determine that here
    if character.race == 'dragonborn':
        character.strength += 2
        character.constitution += 1
    elif character.race == 'dwarf':
        character.constitution += 2
    elif character.race == 'elf':
        character.dexterity += 2
    elif character.race == 'half-elf':
        character.charisma += 2
        character.dexterity += 1
        character.wisdom += 1
    elif character.race == 'gnome':
        character.intelligence += 2
    elif character.race == 'halfling':
        character.dexterity += 2
    elif character.race == 'half-orc':
        character.strength += 2
        character.constitution += 1
    elif character.race == 'human':
        character.strength += 1
        character.dexterity += 1
        character.intelligence += 1
        character.charisma += 1
        character.wisdom += 1
        character.constitution += 1
    elif character.race == 'tiefling':
        character.charisma += 2
        character.intelligence += 1


         # now convert the above stats into -5 to +5, for displaying purposes
    bonus = {10:5, 9:4, 8:3, 7:2, 6:1, 5:0, 4:-1, 3:-2, 2:-3, 1:-4, 0:-5}

    charisma_bonus = bonus[ceil(character.charisma/2)]
    strength_bonus = bonus[ceil(character.strength/2)]
    dexterity_bonus = bonus[ceil(character.dexterity/2)]
    intelligence_bonus = bonus[ceil(character.intelligence/2)]
    wisdom_bonus = bonus[ceil(character.wisdom/2)]
    constitution_bonus = bonus[ceil(character.constitution/2)]

        # now determine the saving throw bonus depending on proficiencies 
        # which we know from the chosen class
    str_save = strength_bonus
    con_save = constitution_bonus
    dex_save = dexterity_bonus
    wis_save = wisdom_bonus
    int_save = intelligence_bonus
    cha_save = charisma_bonus
    if character.class_ == 'Barbarian':
        str_save += proficiency
        con_save += proficiency
    elif character.class_ == 'Bard':
        dex_save += proficiency
        cha_save += proficiency
    elif character.class_ == 'Cleric':
        wis_save += proficiency
        cha_save += proficiency
    elif character.class_ == 'Druid':
        wis_save += proficiency
        int_save += proficiency
    elif character.class_ == 'Fighter':
        str_save += proficiency
        con_save += proficiency
    elif character.class_ == 'Monk':
        str_save += proficiency
        dex_save += proficiency
    elif character.class_ == 'Paladin':
        str_save += proficiency
        cha_save += proficiency
    elif character.class_ == 'Ranger':
        dex_save += proficiency
        wis_save += proficiency
    elif character.class_ == 'Rogue':
        dex_save += proficiency
        int_save += proficiency
    elif character.class_ == 'Sorcerer':
        con_save += proficiency
        cha_save += proficiency
    elif character.class_ == 'Warlock':
        wis_save += proficiency
        cha_save += proficiency
    elif character.class_ == 'Wizard':
        wis_save += proficiency
        int_save += proficiency

        # finally, work out all relevant ability scores from their base stats and proficiencies
        # first set all the stats to base, then check for proficiencies and update
    initiative_score = dexterity_bonus
    acrobatics = dexterity_bonus
    animal_handling = wisdom_bonus
    arcana = intelligence_bonus
    athletics = strength_bonus
    deception = charisma_bonus
    history = intelligence_bonus
    insight = wisdom_bonus
    intimidation = charisma_bonus
    investigation = intelligence_bonus
    medicine = wisdom_bonus
    nature = intelligence_bonus
    perception = wisdom_bonus
    performance = charisma_bonus
    persuasion = charisma_bonus
    religion = intelligence_bonus
    sleight_of_hand = dexterity_bonus
    stealth = dexterity_bonus
    survival = wisdom_bonus
    if character.fi_ability_check == 'acrobatics' or character.se_ability_check == 'acrobatics' or character.th_ability_check == 'acrobatics':
        acrobatics += proficiency
    elif character.fi_ability_check == 'animal handling' or character.se_ability_check == 'animal handling' or character.th_ability_check == 'animal handling':
        animal_handling += proficiency
    elif character.fi_ability_check == 'arcana' or character.se_ability_check == 'arcana' or character.th_ability_check == 'arcana':
        arcana += proficiency
    elif character.fi_ability_check == 'athletics' or character.se_ability_check == 'athletics' or character.th_ability_check == 'athletics':
        athletics += proficiency
    elif character.fi_ability_check == 'deception' or character.se_ability_check == 'deception' or character.th_ability_check == 'deception':
        deception += proficiency
    elif character.fi_ability_check == 'history' or character.se_ability_check == 'history' or character.th_ability_check == 'history':
        history += proficiency
    elif character.fi_ability_check == 'insight' or character.se_ability_check == 'insight' or character.th_ability_check == 'insight':
        insight += proficiency
    elif character.fi_ability_check == 'intimidation' or character.se_ability_check == 'intimidation' or character.th_ability_check == 'intimidation':
        intimidation += proficiency
    elif character.fi_ability_check == 'investigation' or character.se_ability_check == 'investigation' or character.th_ability_check == 'investigation':
        investigation += proficiency
    elif character.fi_ability_check == 'medicine' or character.se_ability_check == 'medicine' or character.th_ability_check == 'medicine':
        medicine += proficiency
    elif character.fi_ability_check == 'nature' or character.se_ability_check == 'nature' or character.th_ability_check == 'nature':
        nature += proficiency
    elif character.fi_ability_check == 'perception' or character.se_ability_check == 'perception' or character.th_ability_check == 'perception':
        perception += proficiency
    elif character.fi_ability_check == 'performance' or character.se_ability_check == 'performance' or character.th_ability_check == 'performance':
        performance += proficiency
    elif character.fi_ability_check == 'persuasion' or character.se_ability_check == 'persuasion' or character.th_ability_check == 'persuasion':
        persuasion += proficiency
    elif character.fi_ability_check == 'religion' or character.se_ability_check == 'religion' or character.th_ability_check == 'religion':
        religion += proficiency
    elif character.fi_ability_check == 'sleight of hand' or character.se_ability_check == 'sleight of hand' or character.th_ability_check == 'sleight of hand':
        sleight_of_hand += proficiency
    elif character.fi_ability_check == 'stealth' or character.se_ability_check == 'stealth' or character.th_ability_check == 'stealth':
        stealth += proficiency
    elif character.fi_ability_check == 'survival' or character.se_ability_check == 'survival' or character.th_ability_check == 'survival':
        survival += proficiency
        
        # now send all the information back to the HTML page to be displayed neatly
    return render_template('charactersheet.html', ptitle='Character Sheet', player=player.forename,\
            name = character.name, level = character.level, class_ = character.class_, race = character.race, proficiency = proficiency,\
            equipment=equipment, strength = strength_bonus, strength_save = str_save, dexterity = dexterity_bonus, dexterity_save = dex_save, \
            intelligence = intelligence_bonus, intelligence_save = int_save, charisma = charisma_bonus, charisma_save = cha_save, \
            constitution = constitution_bonus, constitution_save = con_save, wisdom = wisdom_bonus, wisdom_save = wis_save, 
            initiative = initiative_score, acrobatics = acrobatics, animal_handling = animal_handling, athletics = athletics, arcana = arcana, \
            deception = deception, history = history, insight = insight, intimidation = intimidation, investigation = investigation, medicine = medicine, \
            nature = nature, perception = perception, performance = performance, persuasion = persuasion, religion = religion, \
            sleight_of_hand = sleight_of_hand, stealth = stealth, survival = survival)



@app.route('/createcharacter', methods=['GET', 'POST'])
def createcharacter():
    Form = CreatePlayerCharacter()
    player_id = Player.query.all()
    Form.player_id.choices.extend([(player.player_id, str(player)) for player in player_id])
    if request.method == 'POST':
        # set the associated player to the character
        fk_player_id = Form.player_id.data
        # set the name, level, race and class
        name = Form.name.data
        level = Form.level.data
        class_ = Form.class_.data
        race = Form.race.data

        # now set the str, dex, int, wis, cha, con and int scores
        strength = Form.strength.data
        dexterity = Form.dexterity.data
        wisdom = Form.wisdom.data
        charisma = Form.charisma.data
        constitution = Form.constitution.data
        intelligence = Form.intelligence.data

        # finally allow the choice of up to three ability check proficiencies
        fi_ability_check = Form.fi_ability_check.data
        se_ability_check = Form.se_ability_check.data
        th_ability_check = Form.th_ability_check.data

        #now create the character, add to db and commit 
        new_character = Player_character(fk_player_id=fk_player_id, name=name, level=level, \
            class_=class_,race=race, strength=strength, dexterity=dexterity, wisdom=wisdom, \
            charisma=charisma, constitution=constitution, intelligence=intelligence, \
            fi_ability_check=fi_ability_check, se_ability_check=se_ability_check, th_ability_check=th_ability_check)
        db.session.add(new_character)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('createCharacter.html', form=Form, ptitle='Create a new character')
       

@app.route('/deletecharacter/<int:pk>')
def deletecharacter(pk):
    todelete = Player_character.query.get(pk)
    db.session.delete(todelete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route('/updatecharacter/<int:pk>')
def updatecharacter(pk):
    Form = CreatePlayerCharacter()
    character = Player_character.query.get(pk)
    player_id = Player.query.all()
    Form.player_id.choices.extend([(player.player_id, str(player)) for player in player_id])
    if request.method == 'POST':
        character.fk_player_id = Form.player_id.data

        character.name = Form.name.data
        character.level = Form.level.data
        character.class_ = Form.class_.data
        character.race = Form.race.data

        character.strength = Form.strength.data
        character.dexterity = Form.dexterity.data
        character.wisdom = Form.wisdom.data
        character.charisma = Form.charisma.data
        character.constitution = Form.constitution.data
        character.intelligence = Form.intelligence.data


        character.fi_ability_check = Form.fi_ability_check.data
        character.se_ability_check = Form.se_ability_check.data
        character.th_ability_check = Form.th_ability_check.data

        db.session.commit()
        return redirect(url_for('home'))
    return render_template('createCharacter.html', form=Form, ptitle='Update Character')
       
