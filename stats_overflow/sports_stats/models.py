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
    team_conference = models.CharField(max_length=30)
        
    def __str__(self):
            return self.team_name


#NBA Player Models

class NBA_Player_Scoring_Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    PlayerName = models.CharField(max_length=30)
    GamesPlayed = models.CharField(max_length=10)
    GamesStarted = models.CharField(max_length=10)
    MinutesPerGame = models.CharField(max_length=10)
    PointsPerGame = models.CharField(max_length=10)
    FieldGoalsMade = models.CharField(max_length=10)
    FieldGoalsAttempted = models.CharField(max_length=10)
    FieldGoalPercentage = models.CharField(max_length=10)
    ThreePointFieldGoalsMade = models.CharField(max_length=10) 
    ThreePointFieldGoalsAttempted = models.CharField(max_length=10)
    ThreePointFieldGoalPercentage = models.CharField(max_length=10)
    FreeThrowsMade = models.CharField(max_length=10)
    FreeThrowsAttempted = models.CharField(max_length=10)
    FreeThrowPerentage = models.CharField(max_length=10)

class NBA_Player_Assists_Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    PlayerName = models.CharField(max_length=30)
    GamesPlayed = models.CharField(max_length=10)
    GamesStarted = models.CharField(max_length=10)
    TotalAssists = models.CharField(max_length=10)
    AssistsPerGame = models.CharField(max_length=10)
    Turnovers = models.CharField(max_length=10)
    TurnoversPerGame = models.CharField(max_length=10)
    AssistsPerTurnover = models.CharField(max_length=10)

class NBA_Player_Blocks_Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    PlayerName = models.CharField(max_length=30)
    GamesPlayed = models.CharField(max_length=10)
    GamesStarted = models.CharField(max_length=10)
    TotalBlocks = models.CharField(max_length=10)
    BlocksPerGame = models.CharField(max_length=10)

class NBA_Player_Fouls_Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    PlayerName = models.CharField(max_length=30)
    GamesPlayed = models.CharField(max_length=10)
    GamesStarted = models.CharField(max_length=10)
    MinutesPerGame = models.CharField(max_length=10)
    TotalPersonalFouls = models.CharField(max_length=10)
    PersonalFoulsPerGame = models.CharField(max_length=10)
    FlagrantFouls = models.CharField(max_length=10)
    TechnicalFouls = models.CharField(max_length=10)
    Ejections = models.CharField(max_length=10)
    Disqualifications = models.CharField(max_length=10)

class NBA_Player_Rebounds_Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    PlayerName = models.CharField(max_length=30)
    GamesPlayed = models.CharField(max_length=10)
    GamesStarted = models.CharField(max_length=10)
    MinutesPerGame = models.CharField(max_length=10)
    OffensiveRebounds = models.CharField(max_length=10)
    DeffensiveRebounds = models.CharField(max_length=10)
    TotalRebounds = models.CharField(max_length=10)
    ReboundsPerGame = models.CharField(max_length=10)

class NBA_Player_Steals_Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    PlayerName = models.CharField(max_length=30)
    GamesPlayed = models.CharField(max_length=10)
    GamesStarted = models.CharField(max_length=10)
    TotalSteals = models.CharField(max_length=10)
    StealsPerGame = models.CharField(max_length=10)


#NFL Player Models

class NFL_Player_Defense_Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    PlayerName = models.CharField(max_length=30)
    GamesPlayed = models.CharField(max_length=10)
    SoloTackles = models.CharField(max_length=10)
    AssistedTackles = models.CharField(max_length=10)
    TotalTackles = models.CharField(max_length=10)
    Interceptions = models.CharField(max_length=10)
    InterceptionYards = models.CharField(max_length=10)
    LongestInterception = models.CharField(max_length=10)
    InterceptionsReturnedForTouchdowns = models.CharField(max_length=10)
    ForcedFumbles = models.CharField(max_length=10)
    FumbleRecoveries = models.CharField(max_length=10)
    FumbleRecoveriesReturnedForTouchdowns = models.CharField(max_length=10)
    Sacks = models.CharField(max_length=10)
    PassesDefensed = models.CharField(max_length=10)
    Safeties = models.CharField(max_length=10)

class NFL_Player_Kick_Returns_Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    PlayerName = models.CharField(max_length=30)
    GamesPlayed = models.CharField(max_length=10)
    KickOffReturns = models.CharField(max_length=10)
    KickOffReturnYards = models.CharField(max_length=10)
    AverageYardsPerKickOffReturn = models.CharField(max_length=10)
    LongestKickOffReturn = models.CharField(max_length=10)
    KickOffReturnTouchdowns = models.CharField(max_length=10)

class NFL_Player_Kicking_Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    PlayerName = models.CharField(max_length=30)
    GamesPlayed = models.CharField(max_length=10)
    FieldGoalsMade = models.CharField(max_length=10)
    FieldGoalPercentge = models.CharField(max_length=10)
    LongestFieldGoal = models.CharField(max_length=10)
    ExtraPointsMade = models.CharField(max_length=10)
    ExtraPointPercentage = models.CharField(max_length=10)
    KickingPoints = models.CharField(max_length=10)

class NFL_Player_Passing_Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    PlayerName = models.CharField(max_length=30)
    GamesPlayed = models.CharField(max_length=10)
    PassAttempts = models.CharField(max_length=10)
    PassCompletions = models.CharField(max_length=10)
    CompletionPercentage =models.CharField(max_length=10)
    PassingYards = models.CharField(max_length=10)
    PassingYardsPerGame = models.CharField(max_length=10)
    LongestCompletion = models.CharField(max_length=10)
    TouchdownPasses = models.CharField(max_length=10)
    Interceptions = models.CharField(max_length=10)
    TimesSacked = models.CharField(max_length=10)
    SackYardsLost = models.CharField(max_length=10)

class NFL_Player_Punt_Returns_Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    PlayerName = models.CharField(max_length=30)
    GamesPlayed = models.CharField(max_length=10)
    PuntReturns = models.CharField(max_length=10)
    PuntReturnYards = models.CharField(max_length=10)
    AverageYardsPerPuntReturn = models.CharField(max_length=10)
    LongestPuntReturn = models.CharField(max_length=10)
    PuntReturnTouchdowns = models.CharField(max_length=10)
    FairCatches = models.CharField(max_length=10)

class NFL_Player_Punting_Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    PlayerName = models.CharField(max_length=30)
    GamesPlayed = models.CharField(max_length=10)
    Punts = models.CharField(max_length=10)
    PuntingYards = models.CharField(max_length=10)
    LongestPunts = models.CharField(max_length=10)
    AverageYardsPerPunt = models.CharField(max_length=10)
    NetPuntingAverage = models.CharField(max_length=10)
    PuntsInside20 = models.CharField(max_length=10)
    Touchbacks = models.CharField(max_length=10)
    PuntsResultingInAFairCatch = models.CharField(max_length=10)
    PuntsReturned = models.CharField(max_length=10)
    PuntReturnYardsAgainst = models.CharField(max_length=10)
    AverageYardsPerPuntReturn = models.CharField(max_length=10)
    PuntsBlocked = models.CharField(max_length=10)

class NFL_Player_Receiving_Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    PlayerName = models.CharField(max_length=30)
    GamesPlayed = models.CharField(max_length=10)
    Receptions = models.CharField(max_length=10)
    ReceivingYards = models.CharField(max_length=10)
    ReceivingYardsPerGame = models.CharField(max_length=10)
    AverageYardsPerReception = models.CharField(max_length=10)
    LongestReception = models.CharField(max_length=10)
    ReceivingTouchdowns = models.CharField(max_length=10)

class NFL_Player_Rushing_Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    PlayerName = models.CharField(max_length=30)
    GamesPlayed = models.CharField(max_length=10)
    RushingAttempts = models.CharField(max_length=10)
    RushingYards = models.CharField(max_length=10)
    RushingYardsPerGame = models.CharField(max_length=10)
    AverageYardsPerRush = models.CharField(max_length=10)
    RushingTouchdowns = models.CharField(max_length=10)
    LongestRush = models.CharField(max_length=10)

class NFL_Player_Scoring_Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    PlayerName = models.CharField(max_length=30)
    GamesPlayed = models.CharField(max_length=10)
    RushingTouchdowns = models.CharField(max_length=10)
    ReceivingTouchdowns = models.CharField(max_length=10)
    PuntReturnTouchdowns = models.CharField(max_length=10)
    KickOffReturnedTouchdowns = models.CharField(max_length=10)
    InterceptionsReturnedForTouchdowns = models.CharField(max_length=10)
    FumbleRecoveriesReturnedForTouchdowns = models.CharField(max_length=10)
    FieldGoals = models.CharField(max_length=10)
    ExtraPoints = models.CharField(max_length=10)
    Safeties = models.CharField(max_length=10)
    TwoPointConversions = models.CharField(max_length=10)
    TotalPoints = models.CharField(max_length=10)
    PointsPerGame = models.CharField(max_length=10)


#NHL Models

class NHL_Player_Goaltending_Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    PlayerName = models.CharField(max_length=30)
    GamesPlayed = models.CharField(max_length=10)
    GamesStarted = models.CharField(max_length=10)
    GoalsAgainstAverage = models.CharField(max_length=10)
    SavesPercentage = models.CharField(max_length=10)
    GoalsAgainst = models.CharField(max_length=10)
    ShotsAgainst = models.CharField(max_length=10)
    Wins = models.CharField(max_length=10)
    Losses = models.CharField(max_length=10)
    OvertimeLoss = models.CharField(max_length=10)
    Shutout = models.CharField(max_length=10)
    ShootoutGoalsMadeAndAttempted = models.CharField(max_length=10)

class NHL_Player_Penalties_Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    PlayerName = models.CharField(max_length=30)
    GamesPlayed = models.CharField(max_length=10)
    PenaltyMinutes = models.CharField(max_length=10)
    MajorPenalties = models.CharField(max_length=10)
    MinorPenalties = models.CharField(max_length=10)

class NHL_Player_Scoring_Stats(models.Model):
    id = models.IntegerField(primary_key=True)
    PlayerName = models.CharField(max_length=30)
    GamesPlayed = models.CharField(max_length=10)
    Goals = models.CharField(max_length=10)
    Assists = models.CharField(max_length=10)
    Points = models.CharField(max_length=10)
    PlusMinusGoalsScoredForOrAgainstTotal = models.CharField(max_length=10)
    PenaltyMinutes = models.CharField(max_length=10)
    PowerPlayGoals = models.CharField(max_length=10)
    PowerPlayAssists = models.CharField(max_length=10)
    ShortHandedGoals = models.CharField(max_length=10)
    OverTimeGoals = models.CharField(max_length=10)
    GameWinningGoals = models.CharField(max_length=10)
    ShortHandedAssists = models.CharField(max_length=10)
    ShotsOnGoal = models.CharField(max_length=10)
    ShotsOnGoalPercentage = models.CharField(max_length=10)
    TimeOnIcePerGame = models.CharField(max_length=10)
    ShootoutGoalsMadeAndAttempted = models.CharField(max_length=10)

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
    team_conference = models.CharField(max_length=30)
        
    def __str__(self):
        return self.team_name

#class NFL_Players(models.Model):
#   player_id = models.AutoField(primary_key=True)
#    team_id = models.ForeignKey('NBA_Team', on_delete=models.SET_NULL, null=True)
#    fname = models.CharField(max_length=30)
#    lname = models.CharField(max_length=30)
#    passing_yards = models.CharField(max_length=10)
#    passing_average_yards = models.CharField(max_length=10)
#    passing_attempts = models.CharField(max_length=10)
#    passing_completions = models.CharField(max_length=10)

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
    team_conference = models.CharField(max_length=30)

    def __str__(self):
        return self.name

#class NHL_Players(models.Model):
#   player_id = models.AutoField(primary_key=True)
#    team_id = models.ForeignKey('NHL_Team', on_delete=models.SET_NULL, null=True)
#    fname = models.CharField(max_length = 30)
#    lname = models.CharField(max_length = 30)

#class NHL_Skaters(models.Model):
#    player_id = models.AutoField(primary_key=True)
#    team_id = models.ForeignKey('NHL_Team', on_delete=models.SET_NULL, null=True)
#    points = models.CharField(max_length = 10)
#    goals = models.CharField(max_length = 10)
#    assists = models.CharField(max_length = 10)

#class NHL_Goalies(models.Model):
#    player_id = models.AutoField(primary_key=True)
#    team_id = models.ForeignKey('NHL_Team', on_delete=models.SET_NULL, null=True)
#    gaa = models.CharField(max_length = 10)
#    SV_Percent = models.CharField(max_length = 10)
#    shutouts = models.CharField(max_length = 10)

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
