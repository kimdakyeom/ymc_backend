from django.shortcuts import render
from rest_framework import mixins, generics

from articles.serializers import TeamSerializer
from .models import Team

# Create your views here.


class TeamList(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
