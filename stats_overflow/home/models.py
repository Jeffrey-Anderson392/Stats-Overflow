from django.db import models

# Create your models here.

class User:
    def __init__(self, user_id, fname, lname):
        self.user_id = user_id
        self.fname = fname
        self.lname = lname

class NBA_Team:
    def __init__(self, team_id, name):
        self.team_id = team_id
        self.name = name

class NBA_Players:
    def __init__(self, player_id, team_id, fname, lname, player_points, player_rebounds, player_shots):
        self.player_id = player_id
        self.team_id = team_id
        self.fname = fname
        self.lname = lname
        self.player_points = player_points
        self.player_rebounds = player_rebounds
        self.player_shots = player_shots

class User_Favorite_NBA_Team:
    def __init__(self, team_id, user_id):
        self.team_id = team_id
        self.user_id = user_id

class User_Favorite_NBA_Players:
    def __init__(self, player_id, user_id):
        self.player_id = player_id
        self.user_id = user_id

class NFL_Team:
    def __init__(self, team_id, name):
        self.team_id = team_id
        self.name = name

class NFL_Players:
    def __init__(self, player_id, team_id, fname, lname, passing_yards, passing_average_yards, passing_attempts, passing_completions):
        self.player_id = player_id
        self.team_id = team_id
        self.fname = fname
        self.lname = lname
        self.passing_yards = passing_yards
        self.passing_average_yards = passing_average_yards
        self.passing_attempts = passing_attempts
        self.passing_completions = passing_completions

class User_Favorite_NFL_Team:
    def __init__(self, team_id, user_id):
        self.team_id = team_id
        self.user_id = user_id
        
class User_Favorite_NFL_Players:
    def __init__(self, player_id, user_id):
        self.player_id = player_id
        self.user_id = user_id

class NHL_Team:
    def __init__(self, team_id, name):
        self.team_id = team_id
        self.name = name

class NHL_Players:
    def __init__(self, player_id, team_id, fname, lname):
        self.player_id = player_id
        self.team_id = team_id
        self.fname = fname
        self.lname = lname

class NHL_Skaters:
    def __init__(self, player_id, points, goals, assists):
        self.player_id = player_id
        self.points = points
        self.goals = goals
        self.assists = assists

class NHL_Goalies:
    def __init__(self, player_id, gaa, SV_Percent, shutouts):
        self.player_id = player_id
        self.gaa = gaa
        self.SV_Percent = SV_Percent
        self.shutouts = shutouts

class User_Favorite_NHL_Team:
    def __init__(self, team_id, user_id):
        self.team_id =team_id
        self.user_id = user_id

class User_Favorite_NHL_Players:
    def __init__(self, player_id, user_id):
        self.player_id = player_id
        self.user_id = user_id

class Valorant_team:
    def __init__(self, team_id, name):
        self.team_id = team_id
        self.name = name

class Valorant_Players:
    def __init__(self, player_id, team_id, fname, lname, kills, deaths, kd, ACS, Kills_per_round):
        self.player_id = player_id
        self.team_id =  team_id
        self.fname = fname
        self.lname = lname
        self.kills = kills 
        self.deaths = deaths
        self.kd = kd
        self.ACS = ACS
        self.Kills_per_round = Kills_per_round

class User_Favorite_Valorant_Players:
    def __init__(self, player_id, user_id):
        self.player_id = player_id
        self.user_id = user_id

class User_Favorite_Valorant_Team:
    def __init__(self, team_id, user_id):
        self.team_id = team_id
        self.user_id = user_id

"""User- attributes: user_id, fname, lname 

NBA_team- Attributes: team_id, name 
NBA_Players- Attributes: player_id, team_id, fname, lname, player_points, player_rebounds, player_shots 
User_Favorite_NBA_Team- Attributes: team_id, user_id 
User_Favorite_NBA_Players - Attributes: player_id, user_id 

NFL_team- Attributes: team_id, name 
NFL_Players - 
Attributes: player_id, team_id, fname, lname, passing_yards, passing_average_yards, passing_attempts, passing_completions 
User_Favorite_NFL_Team - Attributes: team_id, user_id 
User_Favorite_NFL_Players - Attributes: player_id, user_id 

NHL_team- Attributes: team_id, name 
NHL_players- Attributes: player_id, team_id, fname, lname 
NHL_Skaters- Attributes: player_id, points, goals, assists 
NHL_Goalies- Attributes: player_id, gaa, SV_%, shutouts 
User_Favorite_NHL_Team - Attributes: team_id, user_id 
User_Favorite_NHL_Players- Attributes: player_id, user_id

Valorant_team- Attributes: team_id, name 
Valorant_Players- Attributes: player_id, team_id, fname, lname, kills, deaths, kd, ACS, Kills_per_round 
User_Favorite_Valorant_Team - Attributes: team_id, user_id 
User_Favorite_Valorant_Players- Attributes: player_id, user_id"""