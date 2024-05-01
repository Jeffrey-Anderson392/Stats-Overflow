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


from .models import NFL_Team
from .models import NHL_Team
from .models import NBA_Team

# Create your views here.

def home(request):
    
    return render(request, 'sports_stats/home.html', {})


# This is where the players are viewed
def NFL_Player_View(request, name):
    context = {}
    
    try:
        defense = NFL_Player_Defense_Stats.objects.get(PlayerName=name)
        context['defense'] = defense
    except ObjectDoesNotExist:
        pass

    try:
        kick_returns = NFL_Player_Kick_Returns_Stats.objects.get(PlayerName=name)
        context['kick_returns'] = kick_returns
    except ObjectDoesNotExist:
        pass

    try:
        kicking = NFL_Player_Kicking_Stats.objects.get(PlayerName=name)
        context['kicking'] = kicking
    except ObjectDoesNotExist:
        pass

    try:
        passing = NFL_Player_Passing_Stats.objects.get(PlayerName=name)
        context['passing'] = passing
    except ObjectDoesNotExist:
        pass

    try:
        punt_returns = NFL_Player_Punt_Returns_Stats.objects.get(PlayerName=name)
        context['punt_returns'] = punt_returns
    except ObjectDoesNotExist:
        pass

    try:
        punting = NFL_Player_Punting_Stats.objects.get(PlayerName=name)
        context['punting'] = punting
    except ObjectDoesNotExist:
        pass

    try:
        receiving = NFL_Player_Receiving_Stats.objects.get(PlayerName=name)
        context['receiving'] = receiving
    except ObjectDoesNotExist: 
        pass

    try:
        rushing = NFL_Player_Rushing_Stats.objects.get(PlayerName=name)
        context['rushing'] = rushing
    except ObjectDoesNotExist:
        pass

    try:
        scoring = NFL_Player_Scoring_Stats.objects.get(PlayerName=name)
        context['scoring'] = scoring
    except ObjectDoesNotExist:
        pass
        
        # defense = NFL_Player_Defense_Stats.objects.get(PlayerName=name)
        # kick_returns = NFL_Player_Kick_Returns_Stats.objects.get(PlayerName=name)
        # kicking = NFL_Player_Kicking_Stats.objects.get(PlayerName=name)
        # passing = NFL_Player_Passing_Stats.objects.get(PlayerName=name)
        # punt_returns = NFL_Player_Punt_Returns_Stats.objects.get(PlayerName=name)
        # punting = NFL_Player_Punting_Stats.objects.get(PlayerName=name)
        # receiving = NFL_Player_Receiving_Stats.objects.get(PlayerName=name)
        # rushing = NFL_Player_Rushing_Stats.objects.get(PlayerName=name)
        # scoring = NFL_Player_Scoring_Stats.objects.get(PlayerName=name)
        # context = {
        #     'defense': defense,
        #     'kick_returns': kick_returns,
        #     'kicking': kicking,
        #     'passing': passing,
        #     'punt_returns': punt_returns,
        #     'punting': punting,
        #     'receiving': receiving,
        #     'rushing': rushing,
        #     'scoring': scoring,
        # }
    return render(request, 'sports_stats/NFL_Player.html', context)

def NHL_Player_View(request, name):
    context = {}
    try:
        goaltending = NHL_Player_Goaltending_Stats.objects.get(PlayerName=name)
        context['goaltending'] = goaltending
    except ObjectDoesNotExist:
        pass

    try:
        penalties = NHL_Player_Penalties_Stats.objects.get(PlayerName=name)
        context['penalties'] = penalties
    except ObjectDoesNotExist:
        pass

    try:
        scoring = NHL_Player_Scoring_Stats.objects.get(PlayerName=name)
        context['scoring'] = scoring
    except ObjectDoesNotExist:
        pass

    # goaltending = NHL_Player_Goaltending_Stats.objects.get(PlayerName=name)
    # penalties = NHL_Player_Penalties_Stats.objects.get(PlayerName=name)
    # scoring = NHL_Player_Scoring_Stats.objects.get(PlayerName=name)
    # context = {
    #     'goaltending': goaltending,
    #     'penalties': penalties,
    #    'scoring': scoring,
    # }
    return render(request, 'sports_stats/NHL_Player.html', context)

def NBA_Player_View(request, name):
    context = {}

    try:
        scoring = NBA_Player_Scoring_Stats.objects.get(PlayerName=name)
        context['scoring'] = scoring
    except ObjectDoesNotExist:
        pass

    try:
        steals = NBA_Player_Steals_Stats.objects.get(PlayerName=name)
        context['steals'] = steals
    except:
        pass

    try:
        fouls = NBA_Player_Fouls_Stats.objects.get(PlayerName=name)
        context['fouls'] = fouls
    except ObjectDoesNotExist:
        pass

    try:
        rebounds = NBA_Player_Rebounds_Stats.objects.get(PlayerName=name)
        context['rebounds'] = rebounds
    except ObjectDoesNotExist:
        pass

    try:
        blocks = NBA_Player_Blocks_Stats.objects.get(PlayerName=name)
        context['blocks'] = blocks
    except ObjectDoesNotExist:
        pass

    try:
        assists = NBA_Player_Assists_Stats.objects.get(PlayerName=name)
        context['assists'] = assists
    except ObjectDoesNotExist:
        pass
    # Scoring = NBA_Player_Scoring_Stats.objects.get(PlayerName=name)
    # Steals = NBA_Player_Steals_Stats.objects.get(PlayerName=name)
    # Fouls = NBA_Player_Fouls_Stats.objects.get(PlayerName=name)
    # Rebounds = NBA_Player_Rebounds_Stats.objects.get(PlayerName=name)
    # Blocks = NBA_Player_Blocks_Stats.objects.get(PlayerName=name)
    # Assists = NBA_Player_Assists_Stats.objects.get(PlayerName=name)
    # context = {
    #     'Scoring': Scoring,
    #     'Steals': Steals,
    #     'Fouls': Fouls,
    #     'Rebounds': Rebounds,
    #     'Blocks': Blocks,
    #     'Assists': Assists,
    # }
    return render(request, 'sports_stats/NBA_Player.html', context)



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