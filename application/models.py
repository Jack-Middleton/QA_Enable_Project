from application import db

class DM(db.Model):
    dm_id = db.Column(db.Integer, primary_key=True)
    forename = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    dm_npcs = db.relationship('NPC', backref='dm')
    dm_players = db.relationship('Player', backref='dm')
    def __str__(self):
        return f"{self.dm_id} DM: \n {self.forename} {self.surname} "

class NPC(db.Model):
    npc_id = db.Column(db.Integer, primary_key=True)
    fk_dm_id = db.Column(db.Integer, db.ForeignKey('DM.dm_id'))
    npc_name = db.Column(db.String(255))
    npc_race = db.Column(db.String(255))
    npc_details = db.Column(db.String(1000))
    def __str__(self):
        return f"Associated DM ID: {self.fk_dm_id} \n NPC ID: {self.npc_id} Name:\n\t {self.npc_name} \n Race: \n\t {self.npc_race}\n Details: \n\t {self.npc_details}"

class Player(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    fk_dm_id = db.Column(db.Integer, db.ForeignKey('DM.dm_id'))
    forename = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    player_characters = db.relationship('Player_character', backref='player')
    def __str__(self):
        return f"{self.forename} {self.surname}"

class Player_character(db.Model):
    pc_id = db.Column(db.Integer, primary_key=True)
    fk_player_id = db.Column(db.Integer, db.ForeignKey('player.player_id'))
    pc_spells = db.relationship('Spells', backref='player_character')
    pc_equipment = db.relationship('Equipment', backref='player_character')
    name = db.Column(db.String(255))
    level = db.Column(db.Integer)
    strength = db.Column(db.Integer)
    dexterity = db.Column(db.Integer)
    intelligence = db.Column(db.Integer)
    wisdom = db.Column(db.Integer)
    constitution = db.Column(db.Integer)
    charisma = db.Column(db.Boolean())
    str_save = db.Column(db.Boolean())
    dex_save = db.Column(db.Boolean())
    int_save = db.Column(db.Boolean())
    wis_save = db.Column(db.Boolean())
    con_save = db.Column(db.Boolean())
    char_save = db.Column(db.Boolean())
    # add individual proficiencies / ability checks

class Spells(db.Model):
    spell_id = db.Column(db.Integer, primary_key=True)
    fk_pc_id = db.Column(db.Integer, db.ForeignKey('player_character.pc_id'))
    spell_name = db.Column(db.String(255))
    spell_details = db.Column(db.String(1000))
    spell_level = db.Column(db.Integer)

class Equipment(db.Model):
    equipment_id = db.Column(db.Integer, primary_key=True)
    fk_pc_id = db.Column(db.Integer, db.ForeignKey('player_character.pc_id'))
    equipment_name = db.Column(db.String(255))
    equipment_details = db.Column(db.String(1000))
    is_strength = db.Column(db.Boolean())
    is_dex = db.Column(db.Boolean())
    is_ranged = db.Column(db.Boolean())
    is_d4 = db.Column(db.Boolean())
    is_d6 = db.Column(db.Boolean())
    is_d8 = db.Column(db.Boolean())
    is_d10 = db.Column(db.Boolean())
    is_d12 = db.Column(db.Boolean())
