from django.contrib import admin
from .models import NBA_Players, NBA_Team, NFL_Players, NFL_Team, NHL_Goalies, NHL_Players, NHL_Skaters, NHL_Team
# Register your models here.
admin.site.register(NBA_Players)
admin.site.register(NBA_Team)
admin.site.register(NFL_Players)
admin.site.register(NFL_Team)
admin.site.register(NHL_Goalies)
admin.site.register(NHL_Players)
admin.site.register(NHL_Skaters)
admin.site.register(NHL_Team)