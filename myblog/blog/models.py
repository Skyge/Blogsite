from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200,blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-created_date',)

    def __str__(self):
        return self.title
