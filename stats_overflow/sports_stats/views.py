from django.shortcuts import render
from django.apps import apps
from django.core.exceptions import ObjectDoesNotExist


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

from .models import Valorant_Players


from .models import NFL_Team
from .models import NHL_Team
from .models import NBA_Team

# Create your views here.

def home(request):
    
    return render(request, 'sports_stats/home.html', {})

from django.shortcuts import render
from .models import NFL_Player_Defense_Stats, NFL_Player_Kick_Returns_Stats, NFL_Player_Kicking_Stats, NFL_Player_Passing_Stats, NFL_Player_Punt_Returns_Stats, NFL_Player_Punting_Stats, NFL_Player_Receiving_Stats, NFL_Player_Rushing_Stats, NFL_Player_Scoring_Stats


# This is where the players are viewed
def NFL_Player_View(request, name):
    context = {}
    context['player_name'] = name

    stats_categories = [ 'Defense Stats', 'Kick Returns Stats', 'Kicking Stats', 
        'Passing Stats', 'Punt Returns Stats', 'Punting Stats',
        'Receiving Stats', 'Rushing Stats', 'Scoring Stats'
    ]

    category_models = {
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

    categories_list = [
        NFL_Player_Defense_Stats,
        NFL_Player_Kick_Returns_Stats,
        NFL_Player_Kicking_Stats,
        NFL_Player_Passing_Stats,
        NFL_Player_Punt_Returns_Stats,
        NFL_Player_Punting_Stats,
        NFL_Player_Receiving_Stats,
        NFL_Player_Rushing_Stats,
        NFL_Player_Scoring_Stats
    ]


    # Invert the dictionary for model class name to category name mapping
    model_to_category = {v: k for k, v in category_models.items()}


    newlist = []
    new_category_models = []

    for model_class in categories_list:
        model_name = model_class.__name__  # Get the class name as a string
        category_name = model_to_category.get(model_name)  # Get the category name using the inverted dictionary

        try:
            model_class.objects.get(PlayerName=name)
            if category_name:
                newlist.append(category_name)
                
        except ObjectDoesNotExist:
            pass

    stats_categories = newlist
    


    selected_category = request.GET.get('category')
    stats_data = None
    field_names = []

    if selected_category:
        model_name = category_models[selected_category]
        model = apps.get_model('sports_stats', model_name) 
        stats_data = model.objects.filter(PlayerName=name)
        field_names = [field.name for field in model._meta.fields]

    return render(request, 'sports_stats/NFL_Player.html', {
        "stats_categories": stats_categories,
        "selected_category": selected_category,
        "stats_data": stats_data,
        "field_names": field_names,
        "player_name": name
    })


def NHL_Player_View(request, name):
    context = {}
    context['player_name'] = name

    stats_categories = [
        'Goaltending Stats', 'Penalties Stats', 'Scoring Stats'
    ]
    category_models = {
        'Goaltending Stats': 'NHL_Player_Goaltending_Stats',
        'Penalties Stats': 'NHL_Player_Penalties_Stats',
        'Scoring Stats': 'NHL_Player_Scoring_Stats',
    }
    categories_list = [
        NHL_Player_Goaltending_Stats,
        NHL_Player_Penalties_Stats,
        NHL_Player_Scoring_Stats
    ]
    selected_category = request.GET.get('category')
    stats_data = None
    field_names = []
    if selected_category:
        model_name = category_models[selected_category]
        model = apps.get_model('sports_stats', model_name) 
        stats_data = model.objects.all()
        field_names = [field.name for field in model._meta.fields]

    # Invert the dictionary for model class name to category name mapping
    model_to_category = {v: k for k, v in category_models.items()}


    newlist = []
    new_category_models = []

    for model_class in categories_list:
        model_name = model_class.__name__  # Get the class name as a string
        category_name = model_to_category.get(model_name)  # Get the category name using the inverted dictionary

        try:
            model_class.objects.get(PlayerName=name)
            if category_name:
                newlist.append(category_name)
                
        except ObjectDoesNotExist:
            pass

    stats_categories = newlist
    


    selected_category = request.GET.get('category')
    stats_data = None
    field_names = []

    if selected_category:
        model_name = category_models[selected_category]
        model = apps.get_model('sports_stats', model_name) 
        stats_data = model.objects.filter(PlayerName=name)
        field_names = [field.name for field in model._meta.fields]

    return render(request, 'sports_stats/NHL_Player.html', {
        "stats_categories": stats_categories,
        "selected_category": selected_category,
        "stats_data": stats_data,
        "field_names": field_names,
        "player_name": name
    })

def NBA_Player_View(request, name):
    context = {}
    context['player_name'] = name

    stats_categories = [
        'Team List', 'Scoring Stats', 'Steals Stats', 'Fouls Stats',
        'Rebounds Stats', 'Blocks Stats', 'Assists Stats'
    ]
    category_models = {
        'Team List': 'NBA_Team',
        'Scoring Stats': 'NBA_Player_Scoring_Stats',
        'Steals Stats': 'NBA_Player_Steals_Stats',
        'Fouls Stats': 'NBA_Player_Fouls_Stats',
        'Rebounds Stats': 'NBA_Player_Rebounds_Stats',
        'Blocks Stats': 'NBA_Player_Blocks_Stats',
        'Assists Stats': 'NBA_Player_Assists_Stats',
    }
    categories_list = [
        NBA_Player_Assists_Stats,
        NBA_Player_Blocks_Stats,
        NBA_Player_Fouls_Stats,
        NBA_Player_Rebounds_Stats,
        NBA_Player_Scoring_Stats,
        NBA_Player_Steals_Stats
    ]

    selected_category = request.GET.get('category')
    stats_data = None
    field_names = []
    if selected_category:
        model_name = category_models[selected_category]
        model = apps.get_model('sports_stats', model_name) 
        stats_data = model.objects.filter(PlayerName=name)
        field_names = [field.name for field in model._meta.fields]

    # Invert the dictionary for model class name to category name mapping
    model_to_category = {v: k for k, v in category_models.items()}

    newlist = []
    new_category_models = []

    for model_class in categories_list:
        model_name = model_class.__name__  # Get the class name as a string
        category_name = model_to_category.get(model_name)  # Get the category name using the inverted dictionary

        try:
            model_class.objects.get(PlayerName=name)
            if category_name:
                newlist.append(category_name)
                
        except ObjectDoesNotExist:
            pass

    stats_categories = newlist
    selected_category = request.GET.get('category')
    stats_data = None
    field_names = []

    if selected_category:
        model_name = category_models[selected_category]
        model = apps.get_model('sports_stats', model_name) 
        stats_data = model.objects.filter(PlayerName=name)
        field_names = [field.name for field in model._meta.fields]

    return render(request, 'sports_stats/NBA_Player.html', {
        "stats_categories": stats_categories,
        "selected_category": selected_category,
        "stats_data": stats_data,
        "field_names": field_names,
        "player_name": name
    })

# Here are the sports views

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
    nba_team_list = NBA_Team.objects.all()
    stats_categories = [
        'Team List', 'Scoring Stats', 'Steals Stats', 'Fouls Stats',
        'Rebounds Stats', 'Blocks Stats', 'Assists Stats'
    ]
    category_models = {
        'Team List': 'NBA_Team',
        'Scoring Stats': 'NBA_Player_Scoring_Stats',
        'Steals Stats': 'NBA_Player_Steals_Stats',
        'Fouls Stats': 'NBA_Player_Fouls_Stats',
        'Rebounds Stats': 'NBA_Player_Rebounds_Stats',
        'Blocks Stats': 'NBA_Player_Blocks_Stats',
        'Assists Stats': 'NBA_Player_Assists_Stats',
    }
    selected_category = request.GET.get('category')
    stats_data = None
    field_names = []
    if selected_category:
        model_name = category_models[selected_category]
        model = apps.get_model('sports_stats', model_name) 
        stats_data = model.objects.all()
        field_names = [field.name for field in model._meta.fields]
    
    return render(request, 'sports_stats/NBA.html', {
        "team_list": nba_team_list, 
        "stats_categories": stats_categories,
        "selected_category": selected_category,
        "stats_data": stats_data,
        "field_names": field_names
    })

def NHL(request):
    nhl_team_list = NHL_Team.objects.all()
    stats_categories = [
        'Team List', 'Goaltending Stats', 'Penalties Stats', 'Scoring Stats'
    ]
    category_models = {
        'Team List': 'NHL_Team',
        'Goaltending Stats': 'NHL_Player_Goaltending_Stats',
        'Penalties Stats': 'NHL_Player_Penalties_Stats',
        'Scoring Stats': 'NHL_Player_Scoring_Stats',
    }
    selected_category = request.GET.get('category')
    stats_data = None
    field_names = []
    if selected_category:
        model_name = category_models[selected_category]
        model = apps.get_model('sports_stats', model_name) 
        stats_data = model.objects.all()
        field_names = [field.name for field in model._meta.fields]
    
    return render(request, 'sports_stats/NHL.html', {
        "team_list": nhl_team_list, 
        "stats_categories": stats_categories,
        "selected_category": selected_category,
        "stats_data": stats_data,
        "field_names": field_names
    })

def Valorant(request):
    players = Valorant_Players.objects.all()
    field_names = []
    if Valorant_Players:
        model_name = Valorant_Players
        model = apps.get_model('sports_stats', model_name) 
        stats_data = model.objects.all()
        field_names = [field.name for field in model._meta.fields]
    return render(request, 'sports_stats/Valorant.html', { "player_list": players, "stats_data": stats_data,
        "field_names": field_names })



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