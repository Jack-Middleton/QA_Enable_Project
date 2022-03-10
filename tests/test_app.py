from flask import url_for
from flask_testing import TestCase
from application import app, db
from application.models import *

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
            SECRET_KEY="test secret key",
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self): # run before each test
        db.create_all()
        # create sample objects here
        sample_dm = DM(forename='Jack', surname='Middleton')
        sample_npc = NPC(fk_dm_id=1,npc_name='Jeremy', npc_race='Dragonborn', npc_details='sample details')
        sample_player = Player(fk_dm_id=1,forename='Bob', surname='Smith')
        sample_character = Player_character(fk_player_id=1, name='Greg', class_='Barbarian', race='Half-Orc', \
            level='16', strength='18', dexterity='14', intelligence='8', wisdom='10', charisma='10', \
            constitution='18', fi_ability_check='acrobatics', se_ability_check='animal handling', th_ability_check='arcana')

        # we need a few different levelled players to test the if character.level = <> then proficiency = <> branches 
        # I've also given them different races to test that particular if elif branch and different classes for the same purpose
        # and added extra characters where needed to finish that section off
        sample_character_l4 = Player_character(fk_player_id='None', name='level 4', class_='Bard', race='dragonborn', \
            level='4', strength='18', dexterity='14', intelligence='8', wisdom='10', charisma='10', \
            constitution='18', fi_ability_check='athletics', se_ability_check='deception', th_ability_check='history')

        sample_character_l8 = Player_character(fk_player_id=1, name='level 8', class_='Cleric', race='dwarf', \
            level='8', strength='18', dexterity='14', intelligence='8', wisdom='10', charisma='10', \
            constitution='18', fi_ability_check='insight', se_ability_check='intimidation', th_ability_check='investigation')

        sample_character_l12 = Player_character(fk_player_id=1, name='level 12', class_='Druid', race='elf', \
            level='12', strength='18', dexterity='14', intelligence='8', wisdom='10', charisma='10', \
            constitution='18', fi_ability_check='medicine', se_ability_check='nature', th_ability_check='perception')

        sample_character_l20 = Player_character(fk_player_id=1, name='level 20', class_='Fighter', race='half-elf', \
            level='20', strength='18', dexterity='14', intelligence='8', wisdom='10', charisma='10', \
            constitution='18', fi_ability_check='performance', se_ability_check='persuasion', th_ability_check='religion')

        # this sample_character is to test whether having no spells or equipment associated to them works as intended
        sample_character_s_e = Player_character(fk_player_id=1, name='Boris', class_='Monk', race='gnome', \
            level='16', strength='18', dexterity='14', intelligence='8', wisdom='10', charisma='10', \
            constitution='18', fi_ability_check='sleight of hand', se_ability_check='stealth', th_ability_check='survival')

        sample_character_halfling = Player_character(fk_player_id=1, name='Sample', class_='Paladin', race='halfling', \
            level='16', strength='18', dexterity='14', intelligence='8', wisdom='10', charisma='10', \
            constitution='18', fi_ability_check='Survival', se_ability_check='Intimidation', th_ability_check='Athletics')

        sample_character_half_orc = Player_character(fk_player_id=1, name='half-orc', class_='Ranger', race='half-orc', \
            level='16', strength='18', dexterity='14', intelligence='8', wisdom='10', charisma='10', \
            constitution='18', fi_ability_check='Survival', se_ability_check='Intimidation', th_ability_check='Athletics')

        sample_character_human = Player_character(fk_player_id=1, name='human', class_='Rogue', race='human', \
            level='16', strength='18', dexterity='14', intelligence='8', wisdom='10', charisma='10', \
            constitution='18', fi_ability_check='Survival', se_ability_check='Intimidation', th_ability_check='Athletics')

        sample_character_tiefling = Player_character(fk_player_id=1, name='Tiefling', class_='Sorcerer', race='tiefling', \
            level='16', strength='18', dexterity='14', intelligence='8', wisdom='10', charisma='10', \
            constitution='18', fi_ability_check='Survival', se_ability_check='Intimidation', th_ability_check='Athletics')
        sample_character_warlock = Player_character(fk_player_id=1, name='Warlock', class_='Warlock', race='Tiefling', \
            level='16', strength='18', dexterity='14', intelligence='8', wisdom='10', charisma='10', \
            constitution='18', fi_ability_check='Survival', se_ability_check='Intimidation', th_ability_check='Athletics')
        sample_character_wizard = Player_character(fk_player_id=1, name='Wizard', class_='Wizard', race='Tiefling', \
            level='16', strength='18', dexterity='14', intelligence='8', wisdom='10', charisma='10', \
            constitution='18', fi_ability_check='Survival', se_ability_check='Intimidation', th_ability_check='Athletics')


        sample_spell = Spells(fk_pc_id=1, spell_name='Fireball', spell_details='4D6', spell_level='3')
        # sample_spell_nolevel tests the if self.spell_level == 0 branch of the Spells model
        sample_spell_nolevel = Spells(fk_pc_id=1, spell_name='Guidance', spell_details='Sample Spell', spell_level='0')
        sample_equipment = Equipment(fk_pc_id=1, equipment_name='Longbow', equipment_details='Basic Longbow', \
            is_weapon=True, str_dex='Dexterity', distance='Ranged', dice_type='D8', rarity='Common')
        # sample_equipment_armour tests the if self.isweapon branch of the equipment model
        sample_equipment_armour = Equipment(fk_pc_id=1, equipment_name='Leather Armour', equipment_details='Basic Leather Armour', \
        is_weapon=False, str_dex=None, distance=None, dice_type=None, rarity='Common')
        db.session.add(sample_dm)
        db.session.add(sample_npc)
        db.session.add(sample_player)
        db.session.add(sample_character) # PK: 1
        db.session.add(sample_character_l4) # PK: 2 Race: dragonborn Class: Bard
        db.session.add(sample_character_l8) # PK: 3 Race: dwarf Class: Cleric
        db.session.add(sample_character_l12) # PK: 4 Race: Elf Class: Druid
        db.session.add(sample_character_l20) # PK: 5 Race: Half-Elf Class: Fighter
        db.session.add(sample_character_s_e) # PK: 6 Race: Gnome Class: Monk
        db.session.add(sample_character_halfling) # PK: 7 Race: Halfling Class: Paladin
        db.session.add(sample_character_half_orc) # PK: 8 Race: Half-Orc Class: Ranger
        db.session.add(sample_character_human) # PK: 9 Race: Human Class: Rogue
        db.session.add(sample_character_tiefling) # PK: 10 Race: Tiefling Class: Sorcerer
        db.session.add(sample_character_warlock) # PK: 11 Class: Warlock
        db.session.add(sample_character_wizard) # PK: 12 Class: Wizard
        db.session.add(sample_spell)
        db.session.add(sample_equipment)
        db.session.add(sample_spell_nolevel)
        db.session.add(sample_equipment_armour)
        db.session.commit()

    def tearDown(self): # run after each test
        db.session.remove()
        db.drop_all()



class TestHome(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assert200(response)
        self.assertIn(b'Jack', response.data)

class TestSpells(TestBase):
    def test_no_spells(self):
        spells = Spells.query.all()
        for spell in spells:
            db.session.delete(spell)
        response = self.client.get(url_for('displaycharacter', pk=1))
        self.assert200(response)
        self.assertIn(b'No Spells', response.data)


class TestEquipment(TestBase):
    def test_no_equipment(self):
        equipment = Equipment.query.all()
        for equipment in equipment:
            db.session.delete(equipment)
        response = self.client.get(url_for('displaycharacter', pk=1))
        self.assertIn(b'No Equipment', response.data)


class TestCharacterDisplay(TestBase):
    def test_character_one(self):
        response = self.client.get(url_for('displaycharacter', pk=1))
        self.assert200(response)
        self.assertIn(b'Greg', response.data)
    
    def test_character_two(self):
        response = self.client.get(url_for('displaycharacter', pk=2))
        self.assert200(response)
        self.assertIn(b'level 4', response.data)
        self.assertIn(b'No Equipment', response.data)
        self.assertIn(b'No Spells', response.data)
        self.assertIn(b"None", response.data)
    
    def test_character_three(self):
        response = self.client.get(url_for('displaycharacter', pk=3))
        self.assert200(response)
        self.assertIn(b'level 8', response.data)
    
    def test_character_four(self):
        response = self.client.get(url_for('displaycharacter', pk=4))
        self.assert200(response)
        self.assertIn(b'level 12', response.data)

    def test_character_five(self):
        response = self.client.get(url_for('displaycharacter', pk=5))
        self.assert200(response)
        self.assertIn(b'level 20', response.data)

    def test_character_nospells_noequipment(self):
        response = self.client.get(url_for('displaycharacter', pk=6))
        self.assert200(response)
        self.assertIn(b'Spells', response.data)
        self.assertIn(b'Equipment:', response.data)
    
    def test_character_seven(self):
        response = self.client.get(url_for('displaycharacter', pk=7))
        self.assert200(response)
        self.assertIn(b'halfling', response.data)
    
    def test_character_human(self):
        response = self.client.get(url_for('displaycharacter', pk=8))
        self.assert200(response)
        self.assertIn(b'half-orc', response.data)

    def test_character_halfling(self):
        response = self.client.get(url_for('displaycharacter', pk=9))
        self.assert200(response)
        self.assertIn(b'human', response.data)

    def test_character_tiefling(self):
        response = self.client.get(url_for('displaycharacter', pk=10))
        self.assert200(response)
        self.assertIn(b'tiefling', response.data)

    def test_character_warlock(self):
        response = self.client.get(url_for('displaycharacter', pk=11))
        self.assert200(response)
        self.assertIn(b'Warlock', response.data)

    def test_character_wizard(self):
        response = self.client.get(url_for('displaycharacter', pk=12))
        self.assert200(response)
        self.assertIn(b'Wizard', response.data)

    def test_no_character(self):
        characters = Player_character.query.all()
        for character in characters:
            db.session.delete(character)
        response = self.client.get(url_for('displaycharacter', pk=1))
        self.assert200(response)
        self.assertIn(b'No Character Sheet to display', response.data)

    def test_no_player(self):
        players = Player.query.all()
        for player in players:
            db.session.delete(player)
        response = self.client.get(url_for('displaycharacter', pk=1))
        self.assert200(response)
        self.assertIn(b'None', response.data)


class TestCreateMethods(TestBase):
    def test_create_get_dm(self):
        response = self.client.get(url_for('createdm'))
        self.assert200(response)
        self.assertIn(b'Forename', response.data)

    def test_create_post_dm(self):
        response = self.client.post(
            url_for('createdm'),
            data = dict(forename='Jack', surname='Middleton'),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Jack', response.data)
    
    def test_get_player(self):
        response = self.client.get(url_for('createcharacter'))
        self.assert200(response)
        self.assertIn(b'Current Level', response.data)
    
    def test_create_post_character(self):
        response = self.client.post(
            url_for('createcharacter'),
            data = dict(fk_player_id = 1, name='Jezza', level='10', class_='druid', race='human', \
             strength='18', dexterity='14', intelligence='8', wisdom='10', charisma='10', \
            constitution='18', fi_ability_check='Survival', se_ability_check='Intimidation', th_ability_check='Athletics'),
            follow_redirects = True 
        )
        self.assert200(response)
        self.assertIn(b'Jezza', response.data)
    
    def test_create_get_npc(self):
        response = self.client.get(url_for('createnpc'))
        self.assert200(response)
        self.assertIn(b'Name of NPC', response.data)
    
    def test_create_post_npc(self):
        response = self.client.post(
            url_for('createnpc'),
            data = dict(dm_id=1, npc_name='Boris', npc_race='Tiefling', npc_details='Absolute muppet'),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Boris', response.data)

    def test_create_get_player(self):
        response = self.client.get(url_for('createplayer'))
        self.assert200(response)
        self.assertIn(b'Forename', response.data)
    
    def test_create_post_player(self):
        response = self.client.post(
            url_for('createplayer'),
            data = dict(dm_id=1, forename='Jane', surname='doe'),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Jane', response.data)
    
    def test_create_get_equipment(self):
        response = self.client.get(url_for('createEquipment'))
        self.assert200(response)
        self.assertIn(b'Equipment Name', response.data)
    
    def test_create_post_equipment(self):
        response = self.client.post(
            url_for('createEquipment'),
            data = dict(pc_id=1, equipment_name='Immovable Rod', equipment_details='Its a rod that doesnt move', \
                is_weapon=False, str_dex='None',distance='None', dice_type='None', rarity='Uncommon' ),
                follow_redirects=True
        )
        self.assert200(response)
        self.assertIn(b'Immovable Rod', response.data)
    
    def test_create_get_spell(self):
        response = self.client.get(url_for('createspell'))
        self.assert200(response)
        self.assertIn(b'Spell Name', response.data)
    
    def test_create_post_spell(self):
        response = self.client.post(
            url_for('createspell'),
            data = dict(pc_id=1, spell_name='Guiding Bolt', spell_details='Cleric Spell', spell_level='1'),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Guiding Bolt', response.data)


class TestDeleteMethods(TestBase):
    def test_delete_dm(self):
        response = self.client.get(url_for('deletedm', pk=1), follow_redirects = True)
        self.assert200(response)
        self.assertNotIn(b'Jack', response.data)

    def test_delete_npc(self):
        response = self.client.get(url_for('deletenpc', pk=1), follow_redirects = True)
        self.assert200(response)
        self.assertNotIn(b'Jeremy', response.data)
    
    def test_delete_player(self):
        response = self.client.get(url_for('deleteplayer', pk=1), follow_redirects = True)
        self.assert200(response)
        self.assertNotIn(b'Bob', response.data)

    def test_delete_character(self):
        response = self.client.get(url_for('deletecharacter', pk=1), follow_redirects = True)
        self.assert200(response)
        self.assertNotIn(b'Greg', response.data)
    
    def test_delete_equipment(self):
        response = self.client.get(url_for('deleteEquipment', pk=1), follow_redirects = True)
        self.assert200(response)
        self.assertNotIn(b'Longbow', response.data)

    def test_delete_spell(self):
        response = self.client.get(url_for('deletespell', pk=1), follow_redirects = True)
        self.assert200(response)
        self.assertNotIn(b'Fireball', response.data)
    


class TestSearchMethods(TestBase):
    def test_search_spells(self):
        response = self.client.get(url_for('searchspells', pk=1))
        self.assert200(response)
        self.assertIn(b'Fireball', response.data)
    
    def test_search_no_spells(self):
        spells = Spells.query.all()
        for spell in spells:
            db.session.delete(spell)
        response = self.client.get(url_for('searchspells', pk=1))
        self.assert200(response)
        self.assertIn(b'Greg has no spells!', response.data)

    def test_search_equipment(self):
        response = self.client.get(url_for('searchequipment', pk=1))
        self.assert200(response)
        self.assertIn(b'Longbow', response.data)
    
    def test_search_no_equipment(self):
        equipment = Equipment.query.all()
        for equipment in equipment:
            db.session.delete(equipment)
        response = self.client.get(url_for('searchequipment', pk=1))
        self.assert200(response)
        self.assertIn(b'Greg has no equipment!', response.data)
    
    def test_search_npc(self):
        response = self.client.get(url_for('searchnpc', pk=1))
        self.assert200(response)
        self.assertIn(b'Jeremy', response.data)
    
    def test_search_no_npc(self):
        npcs = NPC.query.all()
        for npc in npcs:
            db.session.delete(npc)
        response = self.client.get(url_for('searchnpc', pk=1))
        self.assert200(response)
        self.assertIn(b'No NPCs to display!', response.data)

    def test_search_player(self):
        response = self.client.get(url_for('searchplayer', pk=1))
        self.assert200(response)
        self.assertIn(b'Bob', response.data)

    def test_search_no_player(self):
        players = Player.query.all()
        for player in players:
            db.session.delete(player)
        response = self.client.get(url_for('searchplayer', pk=1))
        self.assert200(response)
        self.assertIn(b'No Players to display!', response.data)

    def test_search_character(self):
        response = self.client.get(url_for('searchcharacter', pk=1))
        self.assert200(response)
        self.assertIn(b'Greg', response.data)
    
    def test_search_no_character(self):
        characters = Player_character.query.all()
        for character in characters:
            db.session.delete(character)
        response = self.client.get(url_for('searchcharacter', pk=1))
        self.assert200(response)
        self.assertIn(b'No characters to display!', response.data)

class TestUpdateMethods(TestBase):
    def test_get_update_character(self):
        response = self.client.get(url_for('updatecharacter', pk=1))
        self.assert200(response)
        self.assertIn(b'Characters Name', response.data)
    
    def test_create_update_character(self):
        response = self.client.post(
            url_for('updatecharacter', pk=1),
            data = dict(fk_player_id = 1, name='Gregory', level='10', class_='druid', race='human', \
             strength='18', dexterity='14', intelligence='8', wisdom='10', charisma='10', \
            constitution='18', fi_ability_check='Survival', se_ability_check='Intimidation', th_ability_check='Athletics'),
            follow_redirects = True 
        )
        self.assert200(response)
        self.assertIn(b'Gregory', response.data)

    def test_get_update_dm(self):
        response = self.client.get(url_for('updatedm', pk=1))
        self.assert200(response)
        self.assertIn(b'Forename', response.data)
    
    def test_create_update_dm(self):
        response = self.client.post(
            url_for('updatedm', pk=1),
            data = dict(forename='James', surname='Johnson'),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'James', response.data)

    def test_get_update_npc(self):
        response = self.client.get(url_for('updatenpc', pk=1))
        self.assert200(response)
        self.assertIn(b'Name of NPC', response.data)
    
    def test_create_update_npc(self):
        response = self.client.post(
            url_for('updatenpc', pk=1),
            data = dict(dm_id=1, npc_name='Cait', npc_race='Human', npc_details='Irish'),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Cait', response.data)
    
    def test_get_upate_player(self):
        response = self.client.get(url_for('updateplayer', pk=1))
        self.assert200(response)
        self.assertIn(b'Forename', response.data)

    def test_create_update_player(self):
        response = self.client.post(
            url_for('updateplayer', pk=1),
            data = dict(dm_id=1, forename='John', surname='Smith'),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'John', response.data)

    def test_get_update_equip(self):
        response = self.client.get(url_for('updateEquipment', pk=1))
        self.assert200(response)
        self.assertIn(b'Equipment Name', response.data)

    def test_create_update_equip(self):
        response = self.client.post(
            url_for('updateEquipment', pk=1),
            data = dict(pc_id=1, equipment_name='Studded Leather Armour', equipment_details='+1 AC over regular leather', \
                is_weapon=False, str_dex='None', distance='None', dice_type='None', rarity='None'),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Studded Leather Armour', response.data)
    
    def test_get_update_spell(self):
        response = self.client.get(url_for('updatespell', pk=1))
        self.assert200(response)
        self.assertIn(b'Spell Name', response.data)
    
    def test_create_update_spell(self):
        response = self.client.post(
            url_for('updatespell', pk=1),
            data = dict(pc_id=1, spell_name='Firebolt', spell_details='1d10 per ray', spell_level='1'),
            follow_redirects = True
        )
        self.assert200(response)
        self.assertIn(b'Firebolt', response.data)


