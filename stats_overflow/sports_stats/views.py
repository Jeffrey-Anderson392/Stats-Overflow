from django.shortcuts import render
from django.apps import apps



from .models import NBA_Player_Scoring_Stats
from .models import NBA_Player_Steals_Stats
from .models import NBA_Player_Fouls_Stats
from .models import NBA_Player_Rebounds_Stats
from .models import NBA_Player_Blocks_Stats
from .models import NBA_Player_Assists_Stats
#NFL imports
from .models import NFL_Player_Defense_Stats
from .models import NFL_Player_Kick_Returns_Stats
from .models import NFL_Player_Kicking_Stats
from .models import NFL_Player_Passing_Stats
from .models import NFL_Player_Punt_Returns_Stats
from .models import NFL_Player_Punting_Stats
from .models import NFL_Player_Receiving_Stats
from .models import NFL_Player_Rushing_Stats
from .models import NFL_Player_Scoring_Stats
#NHL imports
from .models import NHL_Player_Goaltending_Stats
from .models import NHL_Player_Penalties_Stats
from .models import NHL_Player_Scoring_Stats


from .models import NFL_Team
from .models import NHL_Team
from .models import NBA_Team

# Create your views here.

def home(request):
    
    return render(request, 'sports_stats/home.html', {})


def NFL(request):
    nfl_team_list = NFL_Team.objects.all()
    stats_categories = [
        'Team List', 'Defense Stats', 'Kick Returns Stats', 'Kicking Stats', 
        'Passing Stats', 'Punt Returns Stats', 'Punting Stats',
        'Receiving Stats', 'Rushing Stats', 'Scoring Stats'
    ]
    category_models = {
        'Team List': 'NFL_Team',
        'Defense Stats': 'NFL_Player_Defense_Stats',
        'Kick Returns Stats': 'NFL_Player_Kick_Returns_Stats',
        'Kicking Stats': 'NFL_Player_Kicking_Stats',
        'Passing Stats': 'NFL_Player_Passing_Stats',
        'Punt Returns Stats': 'NFL_Player_Punt_Returns_Stats',
        'Punting Stats': 'NFL_Player_Punting_Stats',
        'Receiving Stats': 'NFL_Player_Receiving_Stats',
        'Rushing Stats': 'NFL_Player_Rushing_Stats',
        'Scoring Stats': 'NFL_Player_Scoring_Stats',
    }

    selected_category = request.GET.get('category')
    stats_data = None
    field_names = []

    if selected_category:
        model_name = category_models[selected_category]
        model = apps.get_model('sports_stats', model_name) 
        stats_data = model.objects.all()
        field_names = [field.name for field in model._meta.fields]

    return render(request, 'sports_stats/NFL.html', {
        "team_list": nfl_team_list, 
        "stats_categories": stats_categories,
        "selected_category": selected_category,
        "stats_data": stats_data,
        "field_names": field_names
    })

def NBA(request):
    return render(request, 'sports_stats/NBA.html', {})

def NHL(request):
    return render(request, 'sports_stats/NHL.html', {})

def Valorant(request):
    return render(request, 'sports_stats/Valorant.html', {})



""" def parse_csv_and_save_to_database(csv_file):
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
     
    parse_csv_and_save_to_database(csv_file_path)
    return HttpResponse("Data imported successfully!") """