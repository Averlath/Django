from django.db import models


class Status(models.Model):
    status = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.status

    class Meta:
        verbose_name_plural = "Status"


class AllianceRaces(models.Model):
    alliance_race = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.alliance_race

    class Meta:
        verbose_name_plural = "Alliance races"


class HordeRaces(models.Model):
    horde_race = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.horde_race

    class Meta:
        verbose_name_plural = "Horde races"


class Class(models.Model):
    class_name = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.class_name

    class Meta:
        verbose_name_plural = "Classes"


class Faction(models.Model):
    faction_name = models.CharField(max_length=8, default="")

    def __str__(self):
        return self.faction_name


class Character(models.Model):
    character_name = models.CharField(max_length=100, default="")
    character_info = models.CharField(max_length=9999, null=True, blank=True)
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)
    character_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True, blank=True)
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


class AllianceCharacter(Character):
    race = models.ForeignKey(AllianceRaces, on_delete=models.CASCADE, null=True, blank=True)


class HordeCharacter(Character):
    race = models.ForeignKey(HordeRaces, on_delete=models.CASCADE, null=True, blank=True)
