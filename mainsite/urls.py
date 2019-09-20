from django.contrib import admin
from django.urls import path, include
from .views import mainsite

urlpatterns = [
    path('home', mainsite.home, name='home'),
    path('gallery', mainsite.Gallery.as_view(), name='gallery'),
    path('services', mainsite.ServicesView.as_view(), name='services'),
    path('', mainsite.News.as_view(), name='news'),
    path('team', mainsite.MeetTheTeamView.as_view(), name='team'),
    path('article/<int:pk>', mainsite.ArticleTemplate.as_view(), name='article'),
    path('videos', mainsite.Videos.as_view(), name='videos'),
    path('newsbycategory/<int:pk>', mainsite.NewsByCategory.as_view(), name='newsbycategory')


]
