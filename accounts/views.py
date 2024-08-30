from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)
        
        if user is not None:
            login(request, user)
            redirect("home")
        else:
            messages.error("invalid username")
            
    return render(request, "accounts/login.html")

def user_logout(request):
    logout(request)
    return redirect("login")