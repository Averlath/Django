from django.contrib import admin

from .models import Page, AllianceCharacter, HordeCharacter


class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "article_created_by", "article_creation_date", "has_image")
    list_filter = ["title"]
    search_fields = ["title"]


class CharacterAdmin(admin.ModelAdmin):
    list_display = ("character_name", "id", "faction", "race", "character_class", "status", "article_creation_date",
                    "has_image", "has_info")
    list_filter = ["race", "character_class"]
    search_fields = ["character_name", "id"]


admin.site.register(Page, PageAdmin)
admin.site.register(AllianceCharacter, CharacterAdmin)
admin.site.register(HordeCharacter, CharacterAdmin)
