from django.urls import path

from .views import home_view, create_taskt_view

app_name = "todolist"
urlpatterns = [
    path('', home_view, name="home"),
    path('create/', create_taskt_view, name="home"),
]