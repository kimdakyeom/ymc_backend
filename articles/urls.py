from django.urls import path, include
from . import views

app_name = "articles"
urlpatterns = [
    path("team/", views.TeamList.as_view()),
]
