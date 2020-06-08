from django.shortcuts import HttpResponse, render, redirect
from .models import *
from .forms import *


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
    article_list = BreakingNews.objects.filter(pub_date__year=year)
    context = {
        'year': year,
        'article_list': article_list
    }
    return render(request, 'newsdate.html', context)


def register(request):
    context = {
        "form": RegistrationForm
    }
    return render(request, 'signup.html', context)


def addUser(request):
    form = RegistrationForm(request.POST)
    if form.is_valid():
        myregister = RegistrationData(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password'],
                                    email=form.cleaned_data['email'],
                                    phone=form.cleaned_data['phone']
                                     )
        myregister.save()
    return  redirect('home')