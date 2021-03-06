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
    fi_ability_check = db.Column(db.String(15))
    se_ability_check = db.Column(db.String(15))
    th_ability_check = db.Column(db.String(15))
    def __str__(self):
        return f"ID: {self.pc_id} || Name: {self.name}, a level {self.level} {self.race} {self.class_}"

class Spells(db.Model):
    spell_id = db.Column(db.Integer, primary_key=True)
    fk_pc_id = db.Column(db.Integer, db.ForeignKey('player_character.pc_id'), nullable= True)
    spell_name = db.Column(db.String(255))
    spell_details = db.Column(db.String(1000))
    spell_level = db.Column(db.String(10))
    def __str__(self):
        if self.spell_level == 0:
            return f"{self.spell_name}, {self.spell_details}. This spell is a Cantrip"
        else:
            return f"{self.spell_name} || Details: {self.spell_details} || Level: {self.spell_level}"

class Equipment(db.Model):
    # currently only has checks for if it is a weapon
    equipment_id = db.Column(db.Integer, primary_key=True)
    fk_pc_id = db.Column(db.Integer, db.ForeignKey('player_character.pc_id'))
    equipment_name = db.Column(db.String(255))
    equipment_details = db.Column(db.String(1000))
    is_weapon = db.Column(db.Boolean)
    # determines if the item is a strength of dex item
    str_dex  = db.Column(db.String(10))
    # is the weapon ranged or melee
    distance = db.Column(db.String(10))
    # what hit dice does the weapon use if any 
    dice_type = db.Column(db.String(10))
    # determines rarity - common through to legendary (inc magic or non)
    rarity = db.Column(db.String(15))
    # revisions
    # add checks for armour / AC buffs
    def __str__(self):
        if self.is_weapon:
            return f"ID: {self.equipment_id} || {self.equipment_name} || A {self.rarity} {self.str_dex} weapon || Range: {self.distance} || On hit: {self.dice_type} "
        else: 
            return f"ID: {self.equipment_id} || {self.equipment_name} || {self.equipment_details}"
    
