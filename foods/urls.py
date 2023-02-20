from django.urls import path, include
from . import views

app_name = "foods"


urlpatterns = [
    path("<int:team_pk>/store/", views.StoreList.as_view()),
    path("<int:team_pk>/store/<int:pk>/", views.StoreDetail.as_view()),
    path(
        "<int:team_pk>/store/<int:store_pk>/review/",
        views.ReviewViewSet.as_view({"post": "create", "get": "list"}),
    ),
    path(
        "<int:team_pk>/store/<int:store_pk>/review/<int:pk>/",
        views.ReviewViewSet.as_view(
            {"put": "update", "patch": "partial_update", "delete": "destroy"}
        ),
    ),
]
