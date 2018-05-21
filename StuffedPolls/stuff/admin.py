from django.contrib import admin

from .models import AllianceCharacter, HordeCharacter, Faction, Status, Class, HordeRaces, AllianceRaces


class CharacterAdmin(admin.ModelAdmin):
    list_display = ["character_name", "id",  "race", "character_class", "level", "status", "article_creation_date",
                    "has_image", "has_info"]
    list_filter = ["race"]
    search_fields = ["character_name", "id"]


class FactionAdmin(admin.ModelAdmin):
    list_display = ["faction_name"]

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 2:
            return False
        else:
            return True


class StatusAdmin(admin.ModelAdmin):
    list_display = ["status"]


class AllianceRacesAdmin(admin.ModelAdmin):
    list_display = ["alliance_race"]

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 7:
            return False
        else:
            return True


class HordeRacesAdmin(admin.ModelAdmin):
    list_display = ["horde_race"]

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 7:
            return False
        else:
            return True


class ClassAdmin(admin.ModelAdmin):
    list_display = ["class_name"]

    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 12:
            return False
        else:
            return True


admin.site.register(AllianceCharacter, CharacterAdmin)
admin.site.register(HordeCharacter, CharacterAdmin)
admin.site.register(Faction, FactionAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(AllianceRaces, AllianceRacesAdmin)
admin.site.register(HordeRaces, HordeRacesAdmin)
admin.site.register(Class, ClassAdmin)
