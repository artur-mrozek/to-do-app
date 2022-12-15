from django.shortcuts import render, redirect, get_object_or_404

from .models import Task

from .forms import TaskForm

# Create your views here.
def home_view(request, *args, **kwargs):
    queryset = Task.objects.all().filter(owner=request.user)
    context = {"tasks": queryset}
    return render(request, "todolist/home.html", context)

def create_task_view(request, *args, **kwargs):
    form = TaskForm(request.POST or None)
    if form.is_valid():
            t = Task(owner=request.user, title=request.POST["title"], description=request.POST["description"], done=request.POST.get("done") == "on")
            t.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "todolist/create_task.html", context)

def update_task_view(request, pk, *args, **kwargs):
    obj = get_object_or_404(Task, id=pk)
    form = TaskForm(request.POST or None, instance=obj)
    if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form": form}
    return render(request, "todolist/create_task.html", context)