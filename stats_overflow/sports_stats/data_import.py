import csv
from sports_stats.models import NBA_Player_Scoring_Stats  # Import your Django model

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
                TotalSteals=row['TotalsSteals'],
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

import_nba_player_scoring_stats('NBA-Scoring.csv')
import_nba_player_steals_stats('NBA-Steals.csv')
import_nba_player_rebounds_stats('NBA-Rebounds.csv')
import_nba_player_fouls_stats('NBA-Fouls.csv')
import_nba_player_blocks_stats('NBA-Blocks.csv')
import_nba_player_assists_stats('NBA-Assists.csv')