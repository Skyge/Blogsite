# *-* coding:utf8 *-*
from django.template.loader import get_template
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from datetime import  datetime
from .models import Article
import random
import pickle

pickle_file = open('my_data.pkl','rb')
quotes = pickle.load(pickle_file)
Qoute = random.choice(quotes)

def Homepage(request):
    template = get_template('index.html')
    posts = Article.objects.all()
    now = datetime.now()
    qoute = Qoute
    html = template.render(locals())
    return HttpResponse(html)

def Showpost(request,category):
    template = get_template('post.html')
    qoute = Qoute
    try:
        post = Article.objects.get(category=category)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
