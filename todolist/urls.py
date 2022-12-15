from django.urls import path

from .views import home_view, create_task_view, update_task_view

app_name = "todolist"
urlpatterns = [
    path('', home_view, name="home"),
    path('create/', create_task_view, name="create"),
    path('<int:pk>', update_task_view, name="update"),
]