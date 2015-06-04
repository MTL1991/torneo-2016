from django.contrib import admin

from django.contrib.auth.admin import UserAdmin

from ppal.models import *



class UserAdmin(UserAdmin):

    list_display = ('username','email', 'id')





admin.site.register(School)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Match)
