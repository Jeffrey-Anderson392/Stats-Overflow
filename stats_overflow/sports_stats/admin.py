from django.contrib import admin
from .models import NBA_Player_Assists_Stats, NBA_Player_Blocks_Stats, NBA_Player_Fouls_Stats, NBA_Player_Rebounds_Stats, NBA_Player_Scoring_Stats, NBA_Player_Steals_Stats, NFL_Player_Defense_Stats, NFL_Player_Kick_Returns_Stats, NFL_Player_Kicking_Stats, NFL_Player_Passing_Stats, NFL_Player_Punt_Returns_Stats, NFL_Player_Punting_Stats, NFL_Player_Receiving_Stats, NFL_Player_Rushing_Stats, NFL_Player_Scoring_Stats, NHL_Player_Goaltending_Stats, NHL_Player_Penalties_Stats, NHL_Player_Scoring_Stats,NHL_Team, NBA_Team, NFL_Team, Valorant_Team, Valorant_Players
# Register your models here.
admin.site.register(NBA_Player_Assists_Stats)
admin.site.register(NBA_Player_Blocks_Stats)
admin.site.register(NBA_Player_Fouls_Stats)
admin.site.register(NBA_Player_Rebounds_Stats)
admin.site.register(NBA_Player_Scoring_Stats)
admin.site.register(NBA_Player_Steals_Stats)
admin.site.register(NFL_Player_Defense_Stats)
admin.site.register(NFL_Player_Kick_Returns_Stats)
admin.site.register(NFL_Player_Kicking_Stats)
admin.site.register(NFL_Player_Passing_Stats)
admin.site.register(NFL_Player_Punt_Returns_Stats)
admin.site.register(NFL_Player_Punting_Stats)
admin.site.register(NFL_Player_Receiving_Stats)
admin.site.register(NFL_Player_Rushing_Stats)
admin.site.register(NFL_Player_Scoring_Stats)
admin.site.register(NHL_Player_Goaltending_Stats)
admin.site.register(NHL_Player_Penalties_Stats)
admin.site.register(NHL_Player_Scoring_Stats)
admin.site.register(NFL_Team)
admin.site.register(NBA_Team)
admin.site.register(NHL_Team)
admin.site.register(Valorant_Team)
admin.site.register(Valorant_Players)