from django.shortcuts import redirect, render
from django.views.generic import TemplateView, DetailView
from ..models import Article, Photo, Category

def home(request):
    return render(request, 'mainsite/home.html')


class Gallery(TemplateView):
    template_name = 'mainsite/gallery.html'


class ServicesView(TemplateView):
    template_name = 'mainsite/services.html'


class MeetTheTeamView(TemplateView):
    template_name = 'mainsite/meet_the_team.html'


class News(TemplateView):
    template_name = 'mainsite/news.html'

    def get_context_data(self, **kwargs):

        articles = Article.objects.order_by('-publish_date')
        articles_list = list(articles)
        first_trending_articles_list = articles_list[0:3]
        second_trending_articles_list = articles_list[4:7]
        third_trending_articles_list = articles_list[7:10]
        print("First trending ", first_trending_articles_list)
        print("Second trending ", second_trending_articles_list)
        print("Third trending ", third_trending_articles_list)
        categories = Category.objects.all()
        super(News, self).get_context_data(**kwargs)
        context = {'articles': articles_list, 'categories': categories,
                   'first_trending_articles': first_trending_articles_list,
                   'second_trending_articles': second_trending_articles_list,
                   'third_trending_articles': third_trending_articles_list}
        return context


class NewsByCategory(TemplateView):
    template_name = 'mainsite/newsbycategory.html'

    def get_context_data(self, **kwargs):
        pk = self.kwargs['pk']
        category = Category.objects.get(pk=pk)
        articles = Article.objects.filter(article_category=category)
        articles_list = list(articles)
        trending_articles_list = articles_list[:9]
        categories = Category.objects.all()
        super(NewsByCategory, self).get_context_data(**kwargs)
        context = {'articles': articles_list, 'categories': categories, 'trending_articles': trending_articles_list}
        return context


class ArticleTemplate(DetailView):
    model = Article
    template_name = 'mainsite/article.html'

    def get_context_data(self, **kwargs):
        article_pk = self.kwargs['pk']
        print(">>>>>>>>>>>> article pk" + str(article_pk))
        article = Article.objects.get(pk=article_pk)
        super(ArticleTemplate, self).get_context_data(**kwargs)
        context = {'article': article}
        return context


class Videos(TemplateView):
    template_name = 'mainsite/videos.html'