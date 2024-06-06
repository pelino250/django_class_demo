import logging

from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from blog.models import Article

logger = logging.getLogger(__name__)


class ArticleList(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        return Article.objects.all().order_by('-created_at')


def article_detail(request, pk):
    try:
        logger.info('Retrieving Article in the DB')
        article = Article.objects.get(pk=pk)
        logger.info(f'Article retrieved: {article}')

    except Article.DoesNotExist:
        logger.debug('Article Does not exist')
        raise Http404('Article does not exist')
    article = Article.objects.get(pk=pk)

    # article = get_object_or_404(Article, pk=pk)

    return render(request,
                  'blog/article_detail.html',
                  {'article': article})
