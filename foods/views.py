from typing_extensions import override
from requests import Response
from rest_framework import generics, viewsets

from articles.models import Team
from .models import Review, Store
from .serializers import ReviewSerializer, StoreSerializer

# Create your views here.


class StoreList(generics.ListAPIView):
    serializer_class = StoreSerializer
    queryset = Store.objects.all()

    @override
    def get_queryset(self):
        team = Team.objects.get(pk=self.kwargs.get("team_pk"))
        return super().get_queryset().filter(stadium=team.stadium)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class StoreDetail(generics.RetrieveAPIView):
    serializer_class = StoreSerializer

    def get_queryset(self):
        return Store.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

    @override
    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user,
            store_name=Store.objects.get(pk=self.kwargs.get("store_pk")),
        )

    @override
    def get_queryset(self):
        return super().get_queryset().filter(store_name=self.kwargs.get("store_pk"))
