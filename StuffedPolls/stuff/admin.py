from django.contrib import admin

from .models import Page, Faction, Race, Character


class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "article_created_by", "article_creation_date", "has_image")
    list_filter = ["title"]
    search_fields = ["title"]


class FactionAdmin(admin.ModelAdmin):
    list_display = ("faction_name", "id", "has_image")
    search_fields = ["faction_name"]


class RacesAdmin(admin.ModelAdmin):
    list_display = ("race_name", "id", "faction",  "has_image")
    list_filter = ["faction"]
    search_fields = ["race_name"]


class CharacterAdmin(admin.ModelAdmin):
    list_display = ("character_name", "id", "allied_with", "race", "status", "has_image")
    list_filter = ["allied_with"]
    search_fields = ["race_name"]


admin.site.register(Page, PageAdmin)
admin.site.register(Faction, FactionAdmin)
admin.site.register(Race, RacesAdmin)
admin.site.register(Character, CharacterAdmin)
