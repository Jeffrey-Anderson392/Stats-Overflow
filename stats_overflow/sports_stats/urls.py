from django.urls import path
from . import views
from .views import import_data_from_csv

urlpatterns = [
    path('', views.home, name='home'),
    path('NFL/', views.NFL, name="NFL"),
    path('NBA/', views.NBA, name="NBA"),
    path('NHL/', views.NHL, name="NHL"),
    path('Valorant/', views.Valorant, name="Valorant"),
    path('import-csv/', import_data_from_csv, name='import-csv')
    
]