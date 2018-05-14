from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=100, default="")
    page_text = models.CharField(max_length=1000, default="")
    article_created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
    article_creation_date = models.DateTimeField('creation_date', null=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    string = "images"

    def __str__(self):
        return self.title

    def has_image(self):
        return True if str(self.image).find(self.string) == 0 else False

    has_image.boolean = True


class Faction(models.Model):
    faction_name = models.CharField(max_length=100, default="")
    faction_info = models.CharField(max_length=1000, default="")
    image = models.ImageField(upload_to='images', null=True, blank=True)
    string = "images"

    def __str__(self):
        return self.faction_name

    def has_image(self):
        return True if str(self.image).find(self.string) == 0 else False

    has_image.boolean = True


Faction_Choices = (
    ('Alliance','Alliance'),
    ('Horde', 'Horde'),
    ('Allied', 'Allied Race'),
)


class Race(models.Model):
    race_name = models.CharField(max_length=100, default="")
    faction = models.CharField(max_length=8, choices=Faction_Choices, default="")
    race_info = models.CharField(max_length=1000, default="")
    image = models.ImageField(upload_to='images', null=True, blank=True)
    string = "images"

    def __str__(self):
        return self.race_name

    def has_image(self):
        return True if str(self.image).find(self.string) == 0 else False

    has_image.boolean = True


Factions = (
    ('Choose', 'Choose...'),
    ('Alliance','Alliance'),
    ('Horde', 'Horde'),
)


Alliance_Races = (
    ('Human','Human'),
    ('Dwarf', 'Dwarf'),
    ('Night Elf', 'Night Elf'),
    ('Gnome', 'Gnome'),
    ('Draenei', 'Draenei'),
    ('Worgen', 'Worgen'),
    ('Pandaren', 'Pandaren'),
)

Horde_Races = (
    ('Orc','Orc'),
    ('Undead', 'Undead'),
    ('Tauren', 'Tauren'),
    ('Troll', 'Troll'),
    ('Blood Elf', 'Blood Elf'),
    ('Goblin', 'Goblin'),
    ('Pandaren', 'Pandaren'),
)


Status_Choices = (
    ('Alive','Alive'),
    ('Dead', 'Dead'),
    ('Incapacitated', 'Incapacitated'),
    ('Unknown', 'Unknown'),
)


class Character(models.Model):
    character_name = models.CharField(max_length=100, default="")
    allied_with = models.CharField(max_length=8, choices=Factions, default="")
    race = ""
    status = models.CharField(max_length=8, choices=Status_Choices, default="")
    image = models.ImageField(upload_to='images', null=True, blank=True)
    string = "images"

    def __str__(self):
        return self.character_name

    def has_image(self):
        return True if str(self.image).find(self.string) == 0 else False
    has_image.boolean = True

    class Meta:
        abstract = True

class AllianceCharacter(Character):
    race = models.CharField(max_length=8, choices=Alliance_Races)


class HordeCharacter(Character):
    race = models.CharField(max_length=8, choices=Horde_Races)

