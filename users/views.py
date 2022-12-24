from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .forms import LoginForm, RegisterForm

# Create your views here.
def login_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect("/")
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        user = authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/user/login/')
    context = {"form": form}
    return render(request, "users/login.html", context)

def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect("/user/login")

def register_view(request, *args, **kwargs):
    if request.user.is_authenticated:
        return redirect("/")
    form = RegisterForm()
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
            user.save()
            login(request, user)
            return redirect('/')
    context = {"form": form}
    return render(request, "users/register.html", context)