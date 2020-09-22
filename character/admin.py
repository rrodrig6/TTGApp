from django.contrib import admin

from .models import Player, Character, Skill

admin.site.register(Player)
admin.site.register(Character)
admin.site.register(Skill)