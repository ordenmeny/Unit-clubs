from django.contrib import admin
from .models import *

common_fields = ('title', 'description', 'slug')


class ClubAdmin(admin.ModelAdmin):
    list_display = common_fields
    list_display_links = common_fields


admin.site.register(Club, ClubAdmin)
admin.site.register(ModelPost)
admin.site.register(EventModel, ClubAdmin)