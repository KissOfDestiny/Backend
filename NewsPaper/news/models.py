from django.db import models


class Post(models.Model):
    news = 'NW'
    article = 'AR'
    Posts = [(news, 'NW'), (article, 'AR'), ('select', 'select')]
    choosing = models.BooleanField(default=False)
    dateCreation = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, unique=True)
    text = models.TextField()
    rating = models.SmallIntegerField(default=0)
