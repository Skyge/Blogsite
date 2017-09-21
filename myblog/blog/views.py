from django.template.loader import get_template
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from datetime import  datetime
from .models import Article

import urllib.request
import json

url = 'http://open.iciba.com/dsapi'
page = urllib.request.urlopen(url).read()
data = page.decode("UTF-8")

data_dict = json.loads(data)
Qoute = data_dict['content']
note_Qoute = data_dict['note']

def Homepage(request):
    template = get_template('index.html')
    posts = Article.objects.all()
    now = datetime.now()
    qoute = Qoute
    note_qoute = note_Qoute
    html = template.render(locals())
    return HttpResponse(html)

def Showpost(request,category):
    template = get_template('post.html')
    qoute = Qoute
    note_qoute = note_Qoute
    try:
        post = Article.objects.get(category=category)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')
