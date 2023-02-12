from django.db import models
from articles.models import Stadium
from django.conf import settings

# 내부 매점
class Store(models.Model):
    name = models.TextField(max_length=30)
    lat = models.TextField()
    lon = models.TextField()
    stadium = models.ForeignKey(
        Stadium, on_delete=models.CASCADE, related_name="Stadium_stores", default=1
    )
    # 판매 품목
    items = models.TextField()
    # 상세 위치
    detail = models.TextField()
