from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login_user(request):
    # if the method is POST
    if request.method == "POST":
        # retrieve the values of username and password passed from login.html
        username = request.POST["username"]
        password = request.POST["password"]

        # authenticate the user
        user = authenticate(username=username, password=password)

        # if user object is not none meaning successfully authenticated
        if user is not None:
            # if authentication is successful login the user, display a message and redirct to home.
            login(request, user)
            messages.success(
                request, "You have been authenticated and successfully logged in."
            )
            return redirect("home")
        else:
            # if authentication is unsuccessful display a message and redirct to login page.
            messages.success(
                request, "Sorry authentication failed and your login was unsuccessful."
            )
            return redirect("login")
    else:
        return render(request, "sports_stats/home.html", {})


def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect("home")



from django import forms
from .forms import SignUpForm


def register_user(request):
    # if request is POST and form is valid, it saves the new user and log's in.
    if request.method == "POST":
        form = SignUpForm(request.POST)
        # check if all the data in form follows the validation rules
        if form.is_valid():
            user = form.save()
            #read the field data from cleaned_data dictionary
            # using names of fields as keyvalues
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            # authenticate and login
            user = authenticate(username=username, password=password)
            login(request, user)

            messages.success(request, "You have successfully registered!")
            return redirect("home")
    # if form is invalid or request is GET (not POST),
    # it renders register.html template with form
    else:
        #creat blank form
        form = SignUpForm()
    return render(request, "accounts/register.html", {"form": form})
