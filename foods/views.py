from django.shortcuts import render
from rest_framework import generics

from articles.models import Team
from .models import Store
from .serializers import StoreSerializer

# Create your views here.


class StoreList(generics.ListAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

    def get_queryset(self):
        team = Team.objects.get(pk=self.kwargs.get("team_pk"))
        return super().get_queryset().filter(stadium=team.stadium)
