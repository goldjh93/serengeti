# from django.shortcuts import render
# from article.models import Article, Like, Comment


# def index(request):
#   articles = Article.objects.all()
#   # like_count = len(Like.objects.filter(article=article))
#   return render(request, 'index.html' ,{'articles': articles})

from django.shortcuts import render
from article.models import Article, Like

def index(request):
    articles = Article.objects.all()
    # article_likes = {}
    # for article in articles:
    #     like_count = len(Like.objects.filter(article=article))
    #     article_likes[article.id] = like_count

    return render(request, 'index.html', {'articles': articles})