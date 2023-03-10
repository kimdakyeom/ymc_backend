from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User
from dj_rest_auth.serializers import UserDetailsSerializer
from articles.models import Team


class CustomUserDetailsSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            "id",
            "nickname",
            "team",
        )


class CustomUserRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField()
    team = serializers.IntegerField()

    def get_cleaned_data(self):
        super(CustomUserRegisterSerializer, self).get_cleaned_data()
        return {
            "email": self.validated_data.get("email", ""),
            "nickname": self.validated_data.get("nickname", ""),
            "team": self.validated_data.get("team", ""),
            "password1": self.validated_data.get("password1", ""),
            "password2": self.validated_data.get("password2", ""),
        }

    def save(self, request):
        user = super().save(request)
        user.nickname = self.data.get("nickname")
        user.team = Team.objects.get(pk=int(self.data.get("team")))
        user.save()
        return user
