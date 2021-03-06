from django.conf import settings

from django import forms
from django.contrib.auth.models import User

import pytz, datetime
import django.utils.timezone as timezone
from django.utils.timezone import activate

from .models import Team, Player, Event, Announcement

class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Username'}))
    email = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm','placeholder':'Password'}))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class UserChangeForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Last Name'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Username'}))
    email = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm','placeholder':'Password'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

class UserResetForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control form-control-sm','placeholder':'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']

class TeamForm(forms.ModelForm):
    team_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Team'}))
    sport = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Sport'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'State'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'City'}))
    
    class Meta:
        model = Team
        fields = ['team_name', 'sport', 'state', 'city']

class UploadTeamAvatarForm(forms.ModelForm):
    avatar = forms.FileField(widget=forms.ClearableFileInput(attrs={'class':'form-control form-control-sm'}))
    
    class Meta:
        model = Team
        fields = ['avatar']

class PlayerForm(forms.ModelForm):
    team = forms.ModelChoiceField(queryset=Team.objects, empty_label=None)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Last Name'}))
    number = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','placeholder':'Number'}))
    
    class Meta:
        model = Player
        fields = ['team', 'role', 'user', 'first_name', 'last_name', 'number']

class UploadPlayerAvatarForm(forms.ModelForm):
    avatar = forms.FileField(widget=forms.ClearableFileInput(attrs={'class':'form-control form-control-sm'}))

    class Meta:
        model = Player
        fields = ['avatar']

class PlayerChangeForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Last Name'}))
    email = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Email'}))
    phone_number = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','placeholder':'Phone Number'}))
    address = forms.CharField(required=False, widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Address'}))
    uin = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','placeholder':'UIN'}))
    usau_id = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class':'form-control form-control-sm','placeholder':'USAU ID'}))

    class Meta:
        model = Player
        fields = ['team', 'first_name', 'last_name', 'email', 'phone_number', 'address', 'uin', 'usau_id']


class EventForm(forms.ModelForm):
    team = forms.ModelChoiceField(queryset=Team.objects, empty_label=None)
    event_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Event Name'}))
    start_date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class':'form-control form-control-sm'}), initial=timezone.now)
    start_time = forms.TimeField(input_formats=['%I:%M %p'], widget=forms.TimeInput(format='%I:%M %p', attrs={'class':'form-control form-control-sm','placeholder':'Time'}), initial=timezone.now)
    end_date = forms.DateField(widget=forms.SelectDateWidget(attrs={'class':'form-control form-control-sm'}), initial=timezone.now)
    end_time = forms.TimeField(input_formats=['%I:%M %p'], widget=forms.TimeInput(format='%I:%M %p', attrs={'class':'form-control form-control-sm','placeholder':'Time'}), initial=timezone.now)
    location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Location'}))
    notes = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'form-control form-control-sm','placeholder':'Add description'}))
    
    class Meta:
        model = Event
        fields = ['team', 'event_name', 'start_date', 'start_time', 'end_date', 'end_time', 'location', 'notes']


class AnnouncementForm(forms.ModelForm):
    team = forms.ModelChoiceField(queryset=Team.objects, empty_label=None)
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control form-control-sm','placeholder':'Title'}))
    post = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control form-control-sm','placeholder':'Write something...'}))
    
    class Meta:
        model = Announcement
        fields = ['team', 'title', 'post']