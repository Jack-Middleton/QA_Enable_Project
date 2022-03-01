from application import db

class DM(db.Model):
    dm_id = db.Column(db.Integer, primary_key=True)
    forename = None
    surname = None
    dm_npcs = db.relationship('NPC', backref='dm')
    dm_players = db.relationship('Player', backref='dm')
    def __str__(self):
        return f"{self.dm_id} DM: \n {self.forename} {self.surname} "

class NPC(db.Model):
    npc_id = db.Column(db.Integer, primary_key=True)
    fk_dm_id = db.Column(db.Integer, db.ForeignKey('DM.dm_id'))
    npc_name = None
    npc_race = None
    npc_details = None
    def __str__(self):
        return f"{self.npc_id} Name:\n\t {self.npc_name} \n Race: \n\t {self.npc_race}\n Details: \n\t {self.npc_details}"

class Player(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    fk_dm_id = db.Column(db.Integer, db.ForeignKey('DM.dm_id'))
    forename = None
    surname = None
    player_characters = db.relationship('Player_character', backref='player')
    def __str__(self):
        return ""

class Player_character(db.Model):
    pc_id = db.Column(db.Integer, primary_key=True)
    fk_player_id = db.Column(db.Integer, db.ForeignKey('player.player_id'))
    pc_spells = db.relationship('Spells', backref='player_character')
    pc_equipment = db.relationship('Equipment', backref='player_character')
    name = None
    level = None
    strength = None
    dexterity = None
    intelligence = None
    wisdom = None
    constitution = None
    charisma = None
    str_save = None
    dex_save = None
    int_save = None
    wis_save = None
    con_save = None
    charisma= None
    # add individual proficiencies / ability checks

class Spells(db.Model):
    spell_id = db.Column(db.Integer, primary_key=True)
    fk_pc_id = db.Column(db.Integer, db.ForeignKey('player_character.pc_id'))
    spell_name = None
    spell_details = None
    spell_level = None

class Equipment(db.Model):
    equipment_id = db.Column(db.Integer, primary_key=True)
    fk_pc_id = db.Column(db.Integer, db.ForeignKey('player_character.pc_id'))
    equipment_name = None
    equipment_details = None
    is_strength = None
    is_dex = None
    is_ranged = None
    is_d4 = None
    is_d6 = None
    is_d8 = None
    is_d10 = None
    is_d12 = None
