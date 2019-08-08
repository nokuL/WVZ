from django.db import models
from django.urls import reverse

# Create your models here.
from django.shortcuts import render


class Article(models.Model):
    article_number = models.IntegerField(default=0)
    article_title = models.CharField(max_length=100)
    article_cover = models.ImageField(upload_to='images/', default='')
    article_paragraph1 = models.TextField(default='', blank=True)
    article_paragraph2 = models.TextField(default='', blank=True)
    article_paragraph3 = models.TextField(default='', blank=True)
    article_paragraph4 = models.TextField(default='', blank=True)
    article_paragraph5 = models.TextField(default='', blank=True)
    article_paragraph6 = models.TextField(default='', blank=True)
    article_paragraph7 = models.TextField(default='', blank=True)

    def __str__(self):
        return self.article_title

    def get_absolute_url(self):
        print(self.pk)
        return reverse('article', kwargs={'pk': self.pk})


class Photo(models.Model):
    photo_title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/', default='')

    def __str__(self):
        return self.photo_title
