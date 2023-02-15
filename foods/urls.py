from django.urls import path, include
from .views import *
from . import views

app_name = "foods"
urlpatterns = [
    path("<int:team_pk>/store/", views.StoreList.as_view()),
]
