from django.shortcuts import render

from .models import Task

# Create your views here.
def home_view(request, *args, **kwargs):
    queryset = Task.objects.all().filter(owner=request.user)
    context = {"tasks": queryset}
    return render(request, "todolist/home.html", context)