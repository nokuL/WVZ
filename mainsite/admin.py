from django.contrib import admin
from .models import Article, Photo, Category
# Register your models here.

admin.site.register(Article)
admin.site.register(Photo)
admin.site.register(Category)