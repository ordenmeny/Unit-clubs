from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'fio')
    list_display_links = ('username', 'fio')


# Register your models here.
admin.site.register(User, UserAdmin)
