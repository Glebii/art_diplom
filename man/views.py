from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages




def register_view(req: HttpRequest):
    if req.user.is_authenticated:
        return redirect("home_page")
    if req.method == "GET":
        return render(req, "register.html")
    elif req.method == "POST":
        user = User.objects.create_user(
            req.POST.get("username"),
            req.POST.get("email"),
            req.POST.get("password"),
            first_name=req.POST.get("first_name"),
            last_name=req.POST.get("last_name"),
        )
        login(req, user)
        return redirect("home_page")


def login_view(req: HttpRequest):
    if req.user.is_authenticated:
        return redirect("home_page")
    if req.method == "GET":
        return render(req, "login.html")
    elif req.method == "POST":
        user = authenticate(
            req, username=req.POST.get("username"), password=req.POST.get("password")
        )
        if user:
            login(req, user)
        else:
            messages.add_message(req, messages.INFO, "Incorrect username | password")
        return redirect("home_page")


def logout_view(req: HttpRequest):
    logout(req)
    return redirect("home_page")
