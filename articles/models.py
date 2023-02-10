from django.db import models
from accounts.models import User

class Article(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    title = models.CharField('제목', max_length=100)
    content = models.TextField('본문')
    created_at = models.DateTimeField('생성시간', auto_now_add=True)
    modified_at = models.DateTimeField('수정시간', auto_now=True)

    class Meta:
        ordering = ["-created_at"]
    

class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField('생성시간', auto_now_add=True)


class Recomment(models.Model):
    article = models.ForeignKey(Article, related_name='recomments', null=False, blank=False, on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    parents = models.ForeignKey(Comment, related_name='soncomments', null=False, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField('생성시간', auto_now_add=True)
    content = models.TextField()
