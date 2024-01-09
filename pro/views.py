from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from django.contrib.auth import authenticate, login


def sidebar(request):
    context = {}
    

    return render(request, 'sidebar.css', context)

def index(request):
    context = {}

    return render(request, 'dashboard.html', context)

def loginView(request):
    context = {}
    if request.method == "POST":
        username_login = request.POST.get('username')
        password_login = request.POST.get('password')
        user = authenticate(request, username=username_login, password=password_login)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')

    return render(request, 'login.html', context)
