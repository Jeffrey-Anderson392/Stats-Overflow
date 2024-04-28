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
                GamesStarted=row['GamesStarted']
            )

# Call the function with the path to your CSV file
import_nba_player_scoring_stats('NBA-Scoring.csv')