# *-* coding:utf8 *-*
from django.template.loader import get_template
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from datetime import  datetime
from .models import Article
import random

quotes = [ '''A ship in port is safe,but that's not what ships are built for. 
               船停在港口就是安全的，但它不是为了停在港口而造的''',
               '''Fear cripples the soul,so you just have to fight it
               恐惧瘫痪一个人的心灵，因此你必须与之奋战''',
               '''The only limit to our realization of tomorrow will be our doubts of today.
               实现明天理想的唯一障碍是今天的疑虑。放手去做吧！''',
               '''Better to light one candle than to curse the darkness.
               与其诅咒黑暗，不如燃起蜡烛。''',
               '''Our destiny offers not the cup of despair,but the chalice of opportunity.
               命运给予我们的不是失望之酒，而是机会之杯。''',
               '''The good seaman is known in bad weather
               惊涛骇浪，方显英雄本色。''',
               '''Good determine what you're going to be.
               人生的奋斗目标决定你将成为怎样的人。''',
               '''Proper preparation solves 80 percent of life's problems.
               适当的准备能解决生活80%的问题。''',
               '''If you are doing your best,you will not have to worry about failure.
               如果你竭尽全力，你就不用担心失败。''',
               '''One way to get the most out of life is to look upon it as an adventure.
               活出生命最大价值的方法就是把它看成一场冒险。''',
               '''We love life,not because we are used to living but because we are used to loving.
               我们热爱生活，不是因为我们习惯于活着，而是因为我们习惯于爱着。''',
               '''Even if you're on the right track,you'll get run over if you just sit here.
               即使你正处在正轨上，但如果你只是坐在原地，也会被别人碾过去。所以请努力向前！''',
               '''The world stands aside to let anyone pass who knows where he is going.
               如果一个人知道自己要去哪里，全世界都会为他让路。''',
               '''Life isn't about waiting for the storm to pass,it's about learning to dance in the rain.
               生活不是等待暴风雨过去，而是要学会在风雨中起舞。''',
               '''Keep your face to the sunshine and you can't see a shadow.
                心若向阳，无谓悲伤。''',
                '''No matter how much i feel lost and hesitated now.I need to live the way i want the last.
                无论我此时是如何的彷徨迷茫，最终，我都要过上自己想要的生活。''',
                '''You were not born a winner,and you were not born a loser.Ypu are what you make yourself be.
                你不是一个天生的赢家，也不是一个天生的失败者；你是你自己创造的你！''',
                '''I walk slowly,but i never walk backward.
                我走的很慢，但我从不后退！''',
                '''Actually it is just in an idea when feel oneself can achieve and can not achieve.
                觉得自己做得到和做不到，往往只在一念之间。''',
                '''Start where you are.Use what you have.Do what you can.
                始于当下，物尽其用，尽你所能！''',
                '''You may delay,but time will not.
                时不我待！'''

    ]
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




