from django.db import models

# Create your models here.
from django.http import HttpResponse
from django.contrib.auth.models import User

def show_user_id(request):
    user = request.user
    if user.is_authenticated:
        return HttpResponse(f"Your user ID is: {user.id}")
    else:
        return HttpResponse("You are not logged in.")