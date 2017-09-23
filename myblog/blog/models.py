from django.db import models
from django.utils import timezone

import markdown


class Article(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    abstract = models.CharField(max_length=200, blank=True)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()


    class Meta:
        ordering = ('-created_time',)


    def save(self, *args, **kwargs):
        if not self.abstract:
            md = markdown.Markdown(extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ])
            self.abstract = strip_tags(md.convert(self.text))[:54]

        super(Article, self).save(*args, **kwargs)
