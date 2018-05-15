from django.contrib import admin

from .models import AllianceCharacter, HordeCharacter, Faction


class CharacterAdmin(admin.ModelAdmin):
    list_display = ["character_name", "id",  "race", "character_class", "status", "article_creation_date",
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


admin.site.register(AllianceCharacter, CharacterAdmin)
admin.site.register(HordeCharacter, CharacterAdmin)
admin.site.register(Faction, FactionAdmin)

# class PageAdmin(admin.ModelAdmin):
#     list_display = ("title", "id", "article_created_by", "article_creation_date", "has_image")
#     list_filter = ["title"]
#     search_fields = ["title"]

# admin.site.register(Page, PageAdmin)
