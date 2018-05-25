from django.db import models


class Status(models.Model):
    status = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.status

    @property
    def is_player(self):
        return self.status.__str__() == 'Player'

    class Meta:
        verbose_name_plural = "Status"


class AllianceRaces(models.Model):
    alliance_race = models.CharField(max_length=10, default="")
    alliance_text = models.CharField(max_length=9999, default="")

    def __str__(self):
        return self.alliance_race

    @property
    def is_race(self):
        return self.alliance_race.__str__() != 'Pandaren'

    @property
    def is_pandaren(self):
        return self.alliance_race.__str__() == 'Pandaren'

    class Meta:
        verbose_name_plural = "Alliance races"


class HordeRaces(models.Model):
    horde_race = models.CharField(max_length=10, default="")
    horde_text = models.CharField(max_length=9999, default="")

    def __str__(self):
        return self.horde_race

    @property
    def is_race(self):
        return self.horde_race.__str__() != 'Pandaren'

    class Meta:
        verbose_name_plural = "Horde races"


class Class(models.Model):
    class_name = models.CharField(max_length=20, default="")
    class_text = models.CharField(max_length=9999, default="")
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name_plural = "Classes"


class Faction(models.Model):
    faction_name = models.CharField(max_length=8, default="")
    faction_text = models.CharField(max_length=9999, default="")

    def __str__(self):
        return self.faction_name


class Character(models.Model):
    character_name = models.CharField(max_length=100, default="")
    character_info = models.CharField(max_length=9999, null=True, blank=True)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE, default="")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default="")
    character_class = models.ForeignKey(Class, on_delete=models.CASCADE, default="")
    level = models.PositiveIntegerField(default=1)
    article_creation_date = models.DateTimeField('creation_date', null=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    string = "images"

    def __str__(self):
        return self.character_name

    def has_image(self):
        return True if str(self.image).find(self.string) is 0 else False
    has_image.boolean = True

    def has_info(self):
        return True if self.character_info is not None else False
    has_info.boolean = True

    class Meta:
        abstract = True
        ordering = ['character_class', 'character_name']


class AllianceCharacter(Character):
    race = models.ForeignKey(AllianceRaces, on_delete=models.CASCADE, default="")


class HordeCharacter(Character):
    race = models.ForeignKey(HordeRaces, on_delete=models.CASCADE, default="")
