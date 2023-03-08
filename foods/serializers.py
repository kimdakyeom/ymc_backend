from dataclasses import field
from .models import *
from rest_framework import serializers


class StoreImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreImage
        fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):
    store_image = StoreImageSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = [
            "name",
            "lat",
            "lon",
            "stadium",
            "items",
            "detail",
            "store_image",
        ]


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
