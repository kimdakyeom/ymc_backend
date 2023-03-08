from dataclasses import field
from .models import *
from rest_framework import serializers

# class ArticleSerializer(serializers.ModelSerializer):


class StadiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadium
        fields = "__all__"


class TeamSerializer(serializers.ModelSerializer):
    stadium = StadiumSerializer(read_only=True)

    class Meta:
        model = Team
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source="user.nickname")

    class Meta:
        model = Article
        fields = "__all__"
