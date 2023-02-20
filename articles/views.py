from django.shortcuts import render, get_object_or_404
from rest_framework import mixins, generics, viewsets
from articles.serializers import *
from .models import Team
from rest_framework.response import Response

class TeamList(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    # permission_classes = [IsOwnerOrReadOnly]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user.nickname)

    # def retrieve(self, request, pk=None):
    #     queryset = Article.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = ArticleSerializer(user)
    #     return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = Article.objects.all().order_by("-pk")
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)