from django.urls import path, include
from . import views
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

app_name = "articles"
router = DefaultRouter()
router.register('', ArticleViewSet)

urlpatterns = [
    path("team/", views.TeamList.as_view()),
    path("", include(router.urls)),
]
