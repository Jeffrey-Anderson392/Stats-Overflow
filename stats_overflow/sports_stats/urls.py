from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.home, name='catalog'), 
    path('NFL/', views.NFL, name="NFL"),
    path('NBA/', views.NBA, name="NBA"),
    path('NHL/', views.NHL, name="NHL"),
    path('Valorant/', views.Valorant, name="Valorant"),
    path('NFL/NFL_Player/<str:name>/', views.NFL_Player_View, name="NFL_Player"),
    path('NBA/NBA_Player/<str:name>/', views.NBA_Player_View, name="NBA_Player"),
    path('NHL/NHL_Player/<str:name>/', views.NHL_Player_View, name="NHL_Player"),
    path('Valorant/Valorant_Player/<str:name>/', views.Valorant_Player_View, name="Valorant_Player")
]