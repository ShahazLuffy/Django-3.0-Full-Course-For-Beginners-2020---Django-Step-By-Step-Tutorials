from django.shortcuts import HttpResponse, render
from .models import *


def newsView(request):
    context = {
        "list_of_news": ["sport", "political", "social"],
        "my_num": 50
    }

    return render(request, 'news.html', context)


def home(request):
    akbarcontect = {

        "name": "Ali Ghaderi Pour"
    }
    return render(request, 'home.html', akbarcontect)


def breakingnews(request):
    obj = BreakingNews.objects.get(id=1)
    data = {
        "newdata": obj
    }
    return render(request, 'breakingnews.html', data)


def newsdate(request):
    return render(request, 'newsdate.html')



def newsdateyear(request, year):
    article_list = NewsDate.objects.filter(pub_date__year=year)
    context = {
        'year': year,
        'article_list': article_list
    }
    return render(request, 'newsdate.html', context)
