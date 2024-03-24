from django.contrib import admin
from .models import *

common_fields = ('title', 'description', 'slug')


class ClubAdmin(admin.ModelAdmin):
    list_display = common_fields
    list_display_links = common_fields


class ClubAdmin2(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_display_links = ('title', 'slug')


admin.site.register(Club, ClubAdmin2)
admin.site.register(ModelPost)
admin.site.register(EventModel, ClubAdmin)
