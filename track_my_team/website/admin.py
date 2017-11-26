# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import User, Team, Player, Event

# Register your models here.
admin.site.register(User)

class TeamAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'sport')
admin.site.register(Team, TeamAdmin)

# class PlayerAdmin(admin.ModelAdmin):
#     list_display = ('number', 'first_name', 'last_name, 'team')
# admin.site.register(Player, PlayerAdmin)
admin.site.register(Player)

class EventAdmin(admin.ModelAdmin):
    list_display = ('date', 'event_name', 'team')
admin.site.register(Event, EventAdmin)