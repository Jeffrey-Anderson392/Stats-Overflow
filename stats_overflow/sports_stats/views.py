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