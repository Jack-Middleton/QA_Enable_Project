from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, SubmitField

class CreateDM(FlaskForm):
    forename = StringField('Forename')
    surname = StringField('Surname')
    submit = SubmitField('Submit')

class CreateNPC(FlaskForm):
    dm_id = SelectField('Associated DM', choices=[])
    npc_list = SelectField("NPC to update", choices=[])
    npc_name = StringField('Name of NPC')
    npc_race = SelectField('NPC Race', choices=[('Dragonborn', 'Dragonborn'), ('Dwarf','Dwarf'), ('Human', 'Human'), \
        ('Elf', 'Elf'), ('Half-Elf', 'Half-Elf'), ('Gnome', 'Gnome'), ('Halfling', 'Halfling'), ('Half-Orc', 'Half-Orc'), ('Human', 'Human'), \
            ('Tiefling', 'Tiefling')] )
    npc_details = StringField('Details of the NPC eg; equipment, basic stats etc.')
    submit = SubmitField('Submit')
