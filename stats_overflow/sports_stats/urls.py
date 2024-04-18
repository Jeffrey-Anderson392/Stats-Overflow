from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('NFL/', views.NFL, name="NFL"),
    path('NBA/', views.NBA, name="NBA"),
    path('NHL/', views.NHL, name="NHL"),
    path('Valorant/', views.Valorant, name="Valorant"),
    
]