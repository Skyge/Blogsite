from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','category','created_date')

admin.site.register(Article,ArticleAdmin)