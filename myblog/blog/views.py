# *-* coding:utf8 *-*
from django.template.loader import get_template
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from datetime import  datetime
from .models import Article



def Homepage(request):
    template = get_template('index.html')
    posts = Article.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def Showpost(request,category):
    template = get_template('post.html')
    try:
        post = Article.objects.get(category=category)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')




