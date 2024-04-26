from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'sports_stats/home.html', {})

def NFL(request):
    return render(request, 'sports_stats/NFL.html', {})

def NBA(request):
    return render(request, 'sports_stats/NBA.html', {})

def NHL(request):
    return render(request, 'sports_stats/NHL.html', {})

def Valorant(request):
    return render(request, 'sports_stats/Valorant.html', {})

import csv
from .models import NFL_Players



def parse_csv_and_save_to_database(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
            for row in reader:
                if 'nfl' in csv_file.lower():
                    player = NFL_Players(
                        name = row['name'],
                        team = row['team'],
                        points = row['points'],
                    )

                elif 'nba' in csv_file.lower():
                    player = NBA_Players(
                        name = row['name'],
                        team = row['team'],
                        points = row['points'],
                    )
                player.save()

def import_data_from_csv(request):
    csv_file_path = '\Users\amack\OneDrive\Documents\GitHub\Stats-Overflow\stats_overflow\sports_stats\NBA' 
    parse_csv_and_save_to_database(csv_file_path)
    return HttpResponse("Data imported successfully!")