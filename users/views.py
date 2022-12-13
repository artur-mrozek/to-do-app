from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.
def login_view(request, *args, **kwargs):
    form = LoginForm()
    print(request.user.is_authenticated)
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