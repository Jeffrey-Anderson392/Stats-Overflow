from django.db import models

# Create your models here.
from django.http import HttpResponse
from django.contrib.auth.models import User

def show_user_id(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"Your user ID is: {user.id}")
    else:
        return HttpResponse("You are not logged in.")

# Create your models here.
from django.db.models import UniqueConstraint # Constrains fields to unique values
from django.db.models.functions import Lower # Returns lower cased value of field

from django.conf import settings

class NBA_Team(models.Model):
        team_number = models.AutoField(primary_key=True)
        team_name = models.CharField(max_length=30)
        
        def __str__(self):
            return self.team_name
    
class NBA_Players(models.Model):
    player_id = models.AutoField(primary_key=True)
    team_id = models.ForeignKey('NBA_Team', on_delete=models.SET_NULL, null=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    player_points = models.CharField(max_length=10)
    player_rebounds = models.CharField(max_length=10)
    player_shots = models.CharField(max_length=10)

# class User_Favorite_NBA_Team:
#     def __init__(self, team_id, user_id):
#         self.team_id = team_id
#         self.user_id = user_id

# class User_Favorite_NBA_Players:
#     def __init__(self, player_id, user_id):
#         self.player_id = player_id
#         self.user_id = user_id

class NFL_Team(models.Model):
    team_number = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=30)
        
    def __str__(self):
        return self.team_name

class NFL_Players(models.Model):
    player_id = models.AutoField(primary_key=True)
    team_id = models.ForeignKey('NBA_Team', on_delete=models.SET_NULL, null=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    passing_yards = models.CharField(max_length=10)
    passing_average_yards = models.CharField(max_length=10)
    passing_attempts = models.CharField(max_length=10)
    passing_completions = models.CharField(max_length=10)

# class User_Favorite_NFL_Team:
#     def __init__(self, team_id, user_id):
#         self.team_id = team_id
#         self.user_id = user_id
        
# class User_Favorite_NFL_Players:
#     def __init__(self, player_id, user_id):
#         self.player_id = player_id
#         self.user_id = user_id

class NHL_Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class NHL_Players(models.Model):
    player_id = models.AutoField(primary_key=True)
    team_id = models.ForeignKey('NHL_Team', on_delete=models.SET_NULL, null=True)
    fname = models.CharField(max_length = 30)
    lname = models.CharField(max_length = 30)

class NHL_Skaters(models.Model):
    player_id = models.AutoField(primary_key=True)
    team_id = models.ForeignKey('NHL_Team', on_delete=models.SET_NULL, null=True)
    points = models.CharField(max_length = 10)
    goals = models.CharField(max_length = 10)
    assists = models.CharField(max_length = 10)

class NHL_Goalies(models.Model):
    player_id = models.AutoField(primary_key=True)
    team_id = models.ForeignKey('NHL_Team', on_delete=models.SET_NULL, null=True)
    gaa = models.CharField(max_length = 10)
    SV_Percent = models.CharField(max_length = 10)
    shutouts = models.CharField(max_length = 10)

# class User_Favorite_NHL_Team:
#     def __init__(self, team_id, user_id):
#         self.team_id =team_id
#         self.user_id = user_id

# class User_Favorite_NHL_Players:
#     def __init__(self, player_id, user_id):
#         self.player_id = player_id
#         self.user_id = user_id

class Valorant_Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Valorant_Players(models.Model):
    player_id = models.AutoField(primary_key=True)
    team_id = models.ForeignKey('Valorant_Team', on_delete=models.SET_NULL, null=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    kills = models.CharField(max_length = 10)
    deaths = models.CharField(max_length = 10)
    kd = models.CharField(max_length = 10)
    ACS = models.CharField(max_length = 10)
    Kills_per_round = models.CharField(max_length = 10)

# class User_Favorite_Valorant_Players:
#     def __init__(self, player_id, user_id):
#         self.player_id = player_id
#         self.user_id = user_id

# class User_Favorite_Valorant_Team:
#     def __init__(self, team_id, user_id):
#         self.team_id = team_id
#         self.user_id = user_id
