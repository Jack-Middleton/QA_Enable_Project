from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired

class CreateDM(FlaskForm):
    forename = StringField('Forename')
    surname = StringField('Surname')
    submit = SubmitField('Submit')

class CreateNPC(FlaskForm):
    dm_id = SelectField('Associated DM', choices=[])
    npc_name = StringField('Name of NPC')
    npc_race = SelectField('NPC Race', choices=[('Dragonborn', 'Dragonborn'), ('Dwarf','Dwarf'), ('Human', 'Human'), \
        ('Elf', 'Elf'), ('Half-Elf', 'Half-Elf'), ('Gnome', 'Gnome'), ('Halfling', 'Halfling'), ('Half-Orc', 'Half-Orc'), ('Human', 'Human'), \
            ('Tiefling', 'Tiefling')] )
    npc_details = StringField('Details of the NPC eg; equipment, basic stats etc.')
    submit = SubmitField('Submit')

class CreatePlayer(FlaskForm):
    dm_id = SelectField('Associated DM', choices=[])
    forename = StringField('Forename')
    surname = StringField('Surname')
    submit = SubmitField('Submit')

class CreateEquipment(FlaskForm):
    pc_id = SelectField('Associated Character', choices=[('None', 'None')])
    equipment_name = StringField('Equipment Name')
    equipment_details = StringField('Equipment Details')
    is_weapon = BooleanField('Is it a weapon?')
    str_dex = SelectField('Which stat does the item use?', choices=[('None', 'None'),('Strength', 'Strength'), ('Dexterity', 'Dexterity')])
    distance = SelectField('is it Ranged / Melee?', choices=[('None', 'None'),('Ranged', 'Ranged'), ('Melee', 'Melee')])
    dice_type = SelectField('Which dice does it use? ', choices=[('None', 'none'),('D4', 'D4'),('D6', 'D6'),('D8', 'D8'),('D10', 'D10'),('D12', 'D12')])
    rarity = SelectField('What rarity is the item?', choices = [('Common', 'Common'), ('Uncommon', 'Uncommon'), ('Rare', 'Rare'), ('Very Rare', 'Very Rare'),\
         ('Legendary', 'Legendary'), ('Artifact', 'Artifact')])
    submit = SubmitField('Submit')

class CreateSpell(FlaskForm):
    pc_id = SelectField('Associated Character', choices=[('None', 'None')])
    spell_name = StringField('Spell Name')
    spell_details = StringField('Spell Details')
    spell_level = SelectField('Spell Level', choices=[('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9')] )
    submit = SubmitField('Submit')


class CreatePlayerCharacter(FlaskForm):
    player_id = SelectField('Associated Player', choices=[], validators=[DataRequired()])
    name = StringField('Characters Name')
    # choices are 1 to 20 hard coded in because levels cannot be lower than 1 or higher than 20
    # this works the same for other stats, but they go up to 24 as some items and abilities allow
    # characters to go past the 20 cap
    level = SelectField('Current Level', choices = [('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),\
        ('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),\
            ('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20')])
    race = SelectField('Race', choices=[('dragonborn', 'dragonborn'), ('dwarf','dwarf'), ('human', 'human'), \
        ('elf', 'elf'), ('half-elf', 'half-elf'), ('gnome', 'gnome'), ('halfling', 'halfling'), ('half-Orc', 'half-orc'), ('human', 'human'), \
            ('tiefling', 'tiefling')] )
    class_ = SelectField('Class', choices=[('Barbarian', 'barbarian'), ('Bard', 'bard'),('Cleric', 'cleric'),('Druid', 'druid'),('Fighter', 'fighter'),  ('Ranger', 'ranger'),\
        ('Monk', 'monk') ,('Paladin', 'paladin'), ('Rogue', 'rogue'), ('Sorcerer', 'sorcerer'), ('Wizard', 'wizard'),('Warlock', 'warlock')])
    strength = SelectField('Strength Score', choices = [('0', '0'), ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),\
        ('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),\
            ('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21', '21'),('22','22')\
                ,('23','23'), ('24','24') ])
    dexterity = SelectField('Dexterity Score', choices = [('0', '0'), ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),\
        ('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),\
            ('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21', '21'),('22','22')\
                ,('23','23'), ('24','24') ])
    constitution = SelectField('Constitution Score', choices = [('0', '0'), ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),\
        ('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),\
            ('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21', '21'),('22','22')\
                ,('23','23'), ('24','24') ])
    wisdom = SelectField('Wisdom Score', choices = [('0', '0'), ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),\
        ('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),\
            ('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21', '21'),('22','22')\
                ,('23','23'), ('24','24') ])
    charisma = SelectField('Charisma Score', choices = [('0', '0'), ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),\
        ('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),\
            ('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21', '21'),('22','22')\
                ,('23','23'), ('24','24') ])
    intelligence = SelectField('Intelligence Score', choices = [('0', '0'), ('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),\
        ('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('11','11'),('12','12'),('13','13'),('14','14'),\
            ('15','15'),('16','16'),('17','17'),('18','18'),('19','19'),('20','20'),('21', '21'),('22','22')\
                ,('23','23'), ('24','24') ])
    # for the ability check proficiencies, the choices for which never change so these will need to be hard-coded in again
    # it was either this or a single Boolean check for each field so while thos looks long and clunky, it felt like the best choice of the two 
    fi_ability_check = SelectField('Select first proficiency',choices=[('None', 'none'), ('Acrobatics','acrobatics'),('Animal Handling','animal handling'),('Arcana','arcana'),('Athletics','athletics')\
        ,('Deception','deception'),('History','history'), ('Insight','insight'),('Intimidation','intimidation'),('Investigation','investigation'),\
            ('Medicine','medicine'),('Nature','nature'),('Perception','perception'),('Performance','performance'),('Persuasion','persuasion'),('Religion','religion'),\
            ('Sleight of hand','sleight of hand'),('Stealth','stealth'),('Survival','survival')] )
    se_ability_check = SelectField('Select second proficiency',choices=[('None', 'none'), ('Acrobatics','acrobatics'),('Animal Handling','animal handling'),('Arcana','arcana'),('Athletics','athletics')\
        ,('Deception','deception'),('History','history'), ('Insight','insight'),('Intimidation','intimidation'),('Investigation','investigation'),\
            ('Medicine','medicine'),('Nature','nature'),('Perception','perception'),('Performance','performance'),('Persuasion','persuasion'),('Religion','religion'),\
            ('Sleight of hand','sleight of hand'),('Stealth','stealth'),('Survival','survival')] )
    th_ability_check = SelectField('Select third proficiency',choices=[('None', 'none'), ('Acrobatics','acrobatics'),('Animal Handling','animal handling'),('Arcana','arcana'),('Athletics','athletics')\
        ,('Deception','deception'),('History','history'), ('Insight','insight'),('Intimidation','intimidation'),('Investigation','investigation'),\
            ('Medicine','medicine'),('Nature','nature'),('Perception','perception'),('Performance','performance'),('Persuasion','persuasion'),('Religion','religion'),\
            ('Sleight of hand','sleight of hand'),('Stealth','stealth'),('Survival','survival')] )
    submit = SubmitField('Submit')
    