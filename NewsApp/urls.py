from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('news/', newsView, name='news'),
    path('breakingnews/', breakingnews, name='breakingnews'),
    path('newsdate/<int:year>', newsdateyear, name='newsdateyear'),
    path('newsdate/', newsdate, name='newsdate'),
    path('signup/', register, name='signup'),
    path('adduser/', addUser, name='adduser')


]
