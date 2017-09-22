
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from .models import Article, Category, Tag
from comments.forms import CommentForm

import urllib.request
import json
import markdown

url = 'http://open.iciba.com/dsapi'
page = urllib.request.urlopen(url).read()
data = page.decode("UTF-8")

data_dict = json.loads(data)
Qoute = data_dict['content']


def homepage(request):
    posts = Article.objects.all()
    now = datetime.now()
    qoute = Qoute
    return render(request, 'index.html', locals())


def showpost(request, pk):
    qoute = Qoute
    post = get_object_or_404(Article, pk=pk)
    post.text = markdown.markdown(post.text,
                                  extensions=[
                                      'markdown.extensions.extra',       # 本身包含很多拓展
                                      'markdown.extensions.codehilite',  # 语法高亮拓展
                                      'markdown.extensions.toc',         # 允许我们自动生成目录
                                  ])

    form = CommentForm()
    comment_list = post.comment_set.all()
    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'post.html', locals())


