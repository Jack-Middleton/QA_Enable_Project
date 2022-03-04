from application import db

class DM(db.Model):
    dm_id = db.Column(db.Integer, primary_key=True)
    forename = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    dm_npcs = db.relationship('NPC', backref='dm')
    dm_players = db.relationship('Player', backref='dm')
    def __str__(self):
        return f"ID: {self.dm_id} || {self.forename} {self.surname} "

class NPC(db.Model):
    npc_id = db.Column(db.Integer, primary_key=True)
    fk_dm_id = db.Column(db.Integer, db.ForeignKey('DM.dm_id'))
    npc_name = db.Column(db.String(255))
    npc_race = db.Column(db.String(255))
    npc_details = db.Column(db.String(1000))
    def __str__(self):
        return f"ID: {self.npc_id} || Name: {self.npc_name} || Race: {self.npc_race} || Details: {self.npc_details}"

class Player(db.Model):
    player_id = db.Column(db.Integer, primary_key=True)
    fk_dm_id = db.Column(db.Integer, db.ForeignKey('DM.dm_id'))
    forename = db.Column(db.String(255))
    surname = db.Column(db.String(255))
    player_characters = db.relationship('Player_character', backref='player')
    def __str__(self):
        return f"ID: {self.player_id} || {self.forename} {self.surname}"

class Player_character(db.Model):
    pc_id = db.Column(db.Integer, primary_key=True)
    fk_player_id = db.Column(db.Integer, db.ForeignKey('player.player_id'))
    pc_spells = db.relationship('Spells', backref='player_character')
    pc_equipment = db.relationship('Equipment', backref='player_character')
    name = db.Column(db.String(255))
    class_ = db.Column(db.String(20))
    race = db.Column(db.String(20))
    level = db.Column(db.Integer)
    strength = db.Column(db.Integer)
    dexterity = db.Column(db.Integer)
    intelligence = db.Column(db.Integer)
    wisdom = db.Column(db.Integer)
    constitution = db.Column(db.Integer)
    charisma = db.Column(db.Integer)
    first_saving_throw = db.Column(db.String(15))
    second_saving_throw = db.Column(db.String(15))
    fi_ability_check = db.Column(db.String(15))
    se_ability_check = db.Column(db.String(15))
    th_ability_check = db.Column(db.String(15))
    def __str__(self):
        return f"ID: {self.pc_id} || Name: {self.name}, a level {self.level} {self.race} {self.class_}"

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
