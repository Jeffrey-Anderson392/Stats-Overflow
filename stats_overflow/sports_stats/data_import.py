import os 
import csv
#NBA imports
from stats_overflow.sports_stats.models import NBA_Player_Scoring_Stats
from stats_overflow.sports_stats.models import NBA_Player_Steals_Stats
from stats_overflow.sports_stats.models import NBA_Player_Fouls_Stats
from stats_overflow.sports_stats.models import NBA_Player_Rebounds_Stats
from stats_overflow.sports_stats.models import NBA_Player_Blocks_Stats
from stats_overflow.sports_stats.models import NBA_Player_Assists_Stats
#NFL imports
from stats_overflow.sports_stats.models import NFL_Player_Defense_Stats
from stats_overflow.sports_stats.models import NFL_Player_Kick_Return_Stats
from stats_overflow.sports_stats.models import NFL_Player_KickingStats
from stats_overflow.sports_stats.models import NFL_Player_Passing_Stats
from stats_overflow.sports_stats.models import NFL_Player_Punt_Returns_Stats
from stats_overflow.sports_stats.models import NFL_Player_Punting_Stats
from stats_overflow.sports_stats.models import NFL_Player_Receiving_Stats
from stats_overflow.sports_stats.models import NFL_Player_Rushing_Stats
from stats_overflow.sports_stats.models import NFL_Player_Scoring_Stats


# NBA imports
def import_nba_player_scoring_stats(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            player_stat = NBA_Player_Scoring_Stats(
                PlayerName=row['Name'],
                GamesPlayed=row['GamesPlayed'],
                GamesStarted=row['GamesStarted'],
                MinutesPerGame=row['MinutesPerGame'],
                PointsPerGame=row['PointsPerGame'],
                FieldGoalsMade=row['FieldGoalsMade'],
                FieldGoalsAttempted=row['FieldGoalsAttempted'],
                FieldGoalPercentage=row['FieldGoalPercentage'],
                ThreePointFieldGoalsMade=row['ThreeFieldGoalsMade'],
                ThreePointFieldGoalsAttempted=row['ThreeFieldGoalsAttempted'],
                ThreePointFieldGoalPercentage=row['ThreeFieldGoalPercentage'],
                FreeThrowsMade=row['FreeThrowsMade'],
                FreeThrowsAttempted=row['FreeThrowsAttempted'],
                FreeThrowPerentage=row['FreeThrowsPercentage']
            )
            player_stat.save()

def import_nba_player_steals_stats(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            player_stat = NBA_Player_Steals_Stats(
                PlayerName=row['Name'],
                GamesPlayed=row['GamesPlayed'],
                GamesStarted=row['GamesStarted'],
                TotalSteals=row['TotalSteals'],
                StealsPerGame=['StealsPerGame']
            )

def import_nba_player_rebounds_stats(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            player_stat = NBA_Player_Rebounds_Stats(
                PlayerName=row['Name'],
                GamesPlayed=row['GamesPlayed'],
                GamesStarted=row['GamesStarted'],
                MinutesPerGame=row['MinutesPerGame'],
                OffensiveRebounds=row['OffensiveRebounds'],
                DeffensiveRebounds=row['DeffensiveRebounds'],
                TotalRebounds=row['TotalRebounds'],
                ReboundsPerGame=row['ReboundsPerGame']
            )

def import_nba_player_fouls_stats(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            player_stat = NBA_Player_Fouls_Stats(
                PlayerName=row['PlayerName'],
                GamesPlayed=row['GamesPlayed'], 
                GamesStarted=row['GamesStarted'], 
                MinutesPerGame=row['MinutesPerGame'], 
                TotalPersonalFouls=row['TotalPersonalFouls'],
                PersonalFoulsPerGame=row['PersonalFoulsPerGame'],
                FlagrantFouls=row['FlagrantFouls'], 
                TechnicalFouls=row['TechnicalFouls'], 
                Ejections=row['Ejections'], 
                Disqualifications=row['Disqualifications']
            )

def import_nba_player_blocks_stats(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            player_stat = NBA_Player_Blocks_Stats(
                PlayerName=row['Name'], 
                GamesPlayed=row['GamesPlayed'], 
                GamesStarted=row['GamesStarted'], 
                TotalBlocks=row['TotalBlocks'], 
                BlocksPerGame=row['BlocksPerGame']
            )

def import_nba_player_assists_stats(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            player_stat = NBA_Player_Assists_Stats(
                PlayerName=row['Name'], 
                GamesPlayed=row['GamesPlayed'], 
                GamesStarted=row['GamesStarted'], 
                TotalAssists=row['TotalAssists'], 
                AssistsPerGame=row['AssistsPerGame'], 
                Turnover=row['Turnover'], 
                TurnoversPerGame=row['TurnoversPerGame'], 
                AssistsPerTurnover=row['AssistsPerTurnover']
            )

# NFL imports
def import_nfl_player_defense_stats(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            player_stat = NFL_Player_Defense_Stats(
                PlayerName=row['Name'], 
                GamesPlayed=row['GamesPlayed'], 
                SoloTackles=row['SoloTackles'], 
                AssistedTackles=row['AssistedTackles'], 
                TotalTackles=row['TotalTackles'], 
                Interceptions=row['Interceptions'], 
                InterceptionYards=row['InterceptionYards'], 
                LongestInterceptions=row['LongestInterceptions'], 
                InterceptionsReturnedForTouchdowns=row['InterceptionsReturnedForTouchdowns'], 
                ForcedFumbles=row['ForcedFumbles'], 
                FumbleRecoveries=row['FumbleRecoveries'], 
                FumbleRecoveriesReturnedForTouchdowns=row['FumbleRecoviesReturnedForTouchdown'], 
                Sacks=row['Sacks'], 
                PassesDefensed=row['PassesDefensed'], 
                Safties=row['Safties']
            )

def import_nfl_player_kick_returns_stats(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            player_stat = NFL_Player_Kick_Returns_Stats(
                PlayerName=row['Name'], 
                GamesPlayed=row['GamesPlayed'], 
                KickOffReturns=row['KickOffReturns'], 
                KickOffReturnYards=row['KickOffReturnYards'], 
                AverageYardsPerKickOffReturn=row['AverageYardsPerKickOffReturn'], 
                LongestKickOffReturn=row['LongestKickOffReturn'], 
                KickOffReturnTouchdowns=row['KickOffReturnTouchdowns']
            )

def import_nfl_player_kicking_stats(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            player_stat = NFL_Player_Kicking_Stats(
                PlayerName=row['Name'], 
                GamesPlayed=row['GamesPlayed'], 
                FieldGoalsMade=row['FieldGoalsMade'], 
                FieldGoalPercentage=row['FieldGoalPercentage'], 
                LongestFieldGoal=row['LongestFieldGoal'], 
                ExtraPointsMade=row['ExtraPointsMade'], 
                ExtraPointPercentage=row['ExtraPointPercentage'], 
                KickingPoints=row['KickingPoints']
            )

def import_nfl_player_passing_stats(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            player_stat = NFL_Player_Passing_Stats(
                PlayerName=row['Name'],
                GamesPlayed=row['GamesPlayed'], 
                PassAttempts=row['PassAttempts'], 
                PassCompletions=row['PassCompletions'], 
                CompletionPercentages=row['CompletionPercentages'], 
                PassingYards=row['PassingYards'], 
                PassingYardsPerGame=row['PassingYardsPerGame'], 
                LongestCompletion=row['LongestCompletion'], 
                TouchdownPasses=row['TouchdownPasses'], 
                Interceptions=row['Interceptions'], 
                TimesSacked=row['TimesSacked'], 
                SackYardsLost=row['SackYardsLost']
            )

def import_nfl_player_punt_returns_stats(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            player_stat = NFL_Player_Punt_Returns_Stats(
                PlayerName=row['Name'], 
                GamesPlayed=row['GamesPlayed'], 
                PuntReturns=row['PuntReturns'], 
                PuntReturnYards=row['PuntReturnYards'], 
                AverageYardsPerPuntReturn=row['AverageYardsPerPuntReturn'], 
                LongestPuntReturn=row['LongestPuntReturn'], 
                PuntReturnTouchdowns=row['PuntReturnTouchdowns'], 
                FairCatches=row['FairCatches']
            )

def import_nfl_player_punting_stats(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            player_stat = NFL_Player_Punting_Stats(
                PlayerName=row['Name'], 
                GamesPlayed=row['GamesPlayed'], 
                Punts=row['Punts'], 
                PuntingYards=row['PuntingYards'], 
                LongestPunts=row['LongestPunts'], 
                AverageYardsPerPunt=row['AverageYardsPerPunt'], 
                NetPuntingAverage=row['NetPuntingAverage'], 
                PuntsInside20=row['PuntsInside20'], 
                Touchbacks=row['Touchbacks'], 
                PuntsResultingInAFairCatch=row['PuntsResultingInAFairCatch'], 
                PuntsReturned=row['PuntsReturned'], 
                PuntReturnYardsAgainst=row['PuntReturnYardsAgainst'], 
                AverageYardsPerPuntReturn=row=['AverageYardsPerPuntReturn'], 
                PuntsBlocked=row['PuntsBlocked']
            )

def import_nfl_player_receiving_stats(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            player_stat = NFL_Player_Receiving_Stats(
                PlayerName=row['Name'], 
                GamesPlayed=row['GamesPlayed'], 
                Receptions=row['Receptions'], 
                ReceivingYards=row['ReceivingYards'], 
                ReceivingYardsPerGame=row['ReceivingYardsPerGame'], 
                AverageYardsPerReception=row['AverageYardsPerReception'], 
                LongestReception=row['LongestReception'],
                ReceivingTouchdowns=row['ReceivingTouchdowns']
            )

def import_nfl_player_rushing_stats(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            player_stat = NFL_Player_Rushing_Stats(
                PlayerName=row['Name'], 
                GamesPlayed=row['GamesPlayed'], 
                RushingAttempts=row['RushingAttempts'], 
                RushingYards=row['RushingYards'], 
                RushingYardsPerGame=row['RushingYardsPerGame'], 
                AverageYardsPerRush=row['AverageYardsPerRush'], 
                RushingTouchdowns=row['RusingTouchdowns'], 
                LongestRush=row['LongestRush']
            )

def import_nfl_player_scoring_stats(csv_file_path):
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            player_stat = NFL_Player_Scoring_Stats(
                PlayerName=row['Name'], 
                GamesPlayed=row['GamesPlayed'], 
                RushingTouchdowns=row['RushingTouchdowns'], 
                ReceivingTouchdowns=row['ReceivingTouchdowns'], 
                PuntReturnTouchdowns=row['PuntReturnTouchdowns'], 
                KickOffReturnedForTouchdowns=row['KickOffReturnedForTouchdowns'], 
                InterceptionsReturnedForTouchdowns=row['InterceptionsReturnedForTouchdowns'], 
                FumbleRecoveriesReturnedForTouchdowns=row['FumbleRecoveriesReturnedForTouchdowns'], 
                FieldGoals=row['FieldGoals'], 
                ExtraPoints=row['ExtraPoints'], 
                Safeties=row['Safeties'], 
                TwoPointConversions=row['TwoPointConversions'], 
                TotalPoints=row['TotalPoints'], 
                PointsPerGame=row['PointsPerGame']
            )

# Calling function with NBA paths
nba_scoring_csv_file_path = os.path.join(os.path.dirname(__file__), 'NBA', 'NBA-Scoring.csv')
import_nba_player_scoring_stats(nba_scoring_csv_file_path)

nba_steals_csv_file_path = os.path.join(os.path.dirname(__file__), 'NBA', 'NBA-Steals.csv')
import_nba_player_steals_stats(nba_steals_csv_file_path)

nba_rebounds_csv_file_path = os.path.join(os.path.dirname(__file__), 'NBA', 'NBA-Rebounds.csv')
import_nba_player_rebounds_stats(nba_rebounds_csv_file_path)


nba_fouls_csv_file_path = os.path.join(os.path.dirname(__file__), 'NBA', 'NBA-Fouls.csv')
import_nba_player_fouls_stats(nba_fouls_csv_file_path)


nba_blocks_csv_file_path = os.path.join(os.path.dirname(__file__), 'NBA', 'NBA-Blocks.csv')
import_nba_player_blocks_stats(nba_blocks_csv_file_path)


nba_assists_csv_file_path = os.path.join(os.path.dirname(__file__), 'NBA', 'NBA-Assists.csv')
import_nba_player_assists_stats(nba_assists_csv_file_path)


#Calling function with NFL paths
nfl_defense_csv_file_path = os.path.join(os.path.dirname(__file__), 'NFL', 'NFL-Defense.csv')
import_nfl_player_defense_stats(nfl_defense_csv_file_path)

nfl_kick_returns_csv_file_path = os.path.join(os.path.dirname(__file__), 'NFL', 'NFL-Kick_Returns.csv')
import_nfl_player_kick_returns_stats(nfl_kick_returns_csv_file_path)

nfl_kicking_csv_file_path = os.path.join(os.path.dirname(__file__), 'NFL', 'NFL-Kicking.csv')
import_nfl_player_kicking_stats(nfl_kicking_csv_file_path)

nfl_passing_csv_file_path = os.path.join(os.path.dirname(__file__), 'NFL', 'NFL-Passing.csv')
import_nfl_player_passing_stats(nfl_passing_csv_file_path)

nfl_punt_returns_csv_file_path = os.path.join(os.path.dirname(__file__), 'NFL', 'NFL-Punt_Returns.csv')
import_nfl_player_punt_returns_stats(nfl_punt_returns_csv_file_path)

nfl_punting_csv_file_path = os.path.join(os.path.dirname(__file__), 'NFL', 'NFL-Punting.csv')
import_nfl_player_punting_stats(nfl_punting_csv_file_path)

nfl_receiving_csv_file_path = os.path.join(os.path.dirname(__file__), 'NFL', 'NFL-Receiving.csv')
import_nfl_player_receiving_stats(nfl_receiving_csv_file_path)

nfl_rushing_csv_file_path = os.path.join(os.path.dirname(__file__), 'NFL', 'NFL-Rushing.csv')
import_nfl_player_rushing_stats(nfl_rushing_csv_file_path)

nfl_scoring_csv_file_path = os.path.join(os.path.dirname(__file__), 'NFL', 'NFL-Scoring.csv')
import_nfl_player_scoring_stats(nfl_scoring_csv_file_path)