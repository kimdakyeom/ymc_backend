from dataclasses import field
from .models import *
from rest_framework import serializers


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):

    store_name = serializers.ReadOnlyField(source="store.pk")
    user = serializers.ReadOnlyField(source="user.nickname")

    class Meta:
        model = Review
        fields = [
            "pk",
            "store_name",
            "content",
            "user",
            "grade",
            "created_at",
        ]
