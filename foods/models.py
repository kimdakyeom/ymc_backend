from django.db import models
from articles.models import Stadium
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator

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


class Review(models.Model):
    store_name = models.ForeignKey(
        Store,
        on_delete=models.CASCADE,
        related_name="store_reviews",
        blank=True,
        null=True,
    )
    content = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_reviews"
    )
    grade = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    created_at = models.DateTimeField(auto_now_add=True)
