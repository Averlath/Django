from django.contrib import admin

from .models import Page

class PageAdmin(admin.ModelAdmin):
    list_display = ("title", "id", "created_by", "creation_date", "has_image")
    list_filter = ["title"]
    search_fields = ["title"]


admin.site.register(Page, PageAdmin)
