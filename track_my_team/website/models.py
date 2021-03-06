# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

import datetime

# Create your models here.

# Team model will store team profile information
class Team(models.Model):
    team_name = models.CharField(max_length=64)
    sport = models.CharField(max_length=64)
    state = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    avatar = models.FileField(default='default.png')

    def __str__(self):
        return self.team_name

    def get_captains(self):
        players = Player.objects.filter(team=self, role="CAPTAIN")
        return players

# Player model will store player profile information
class Player(models.Model):
    user = models.ForeignKey(User, related_name='players', on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name='teams', on_delete=models.CASCADE)
    PLAYER_ROLE = (
        ("CAPTAIN", "Captain"),
        ("PLAYER", "Player")
    )
    role = models.CharField(max_length=7, choices=PLAYER_ROLE, default="PLAYER")
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    number = models.IntegerField(null=True, blank=True)
    email = models.CharField(max_length=64, blank=True)
    phone_number = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=128, blank=True)
    uin = models.IntegerField(null=True, blank=True)
    usau_id = models.IntegerField(null=True, blank=True)
    avatar = models.FileField(default='default.png')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

# Event model will store event detail information
class Event(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    event_name = models.CharField(max_length=64)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    location = models.CharField(max_length=64)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.event_name

# Announcements model will store all announcements
class Announcement(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    post_date = models.DateField(default=datetime.date.today)
    post = models.TextField()

    def __str__(self):
        return self.title
