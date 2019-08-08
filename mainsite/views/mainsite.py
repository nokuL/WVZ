from django.shortcuts import redirect, render
from django.views.generic import TemplateView, DetailView
from ..models import Article, Photo

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

        articles = Article.objects.all()
        articles_list = list(articles)
        super(News, self).get_context_data(**kwargs)
        context = {'articles': articles_list}
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