from django.contrib.auth.models import User
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import CommentForm, ArticleForm
from .models import Article


# Create your views here.

def index(request):
    article = Article.objects.order_by('-article_date')
    return render(request, 'articles/list.html', {'article': article})


def detail(request, article_id):
    try:
        user = User.objects.get(id=request.user.id)
        article = Article.objects.get(id=article_id)
    except:
        return Http404('Статья не найдена')
    latest_comments_list = article.comment_set.order_by('-id')
    form = CommentForm()
    is_liked = False
    if article.likes.filter(id=request.user.id).exists():
        is_liked = True
    return render(request, 'articles/detail.html', {'article': article, 'latest_comments_list': latest_comments_list, 'form': form, 'is_liked': is_liked, 'total_likes': article.total_likes()})


def new_article(request):
    article_form = ArticleForm()
    return render(request, 'articles/new_article.html', {'form_article': article_form})


def add_like(request, article_id):
    try:
        article = Article.objects.get(id=article_id)
    except:
        return Http404('Статья не найдена')
    is_liked = False
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
        is_liked = False
    else:
        article.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(reverse('articles:article', args=(article.id,)))


def leave_comment(request, article_id):
    try:
        user = User.objects.get(username=request.user.get_username())
        article = Article.objects.get(id=article_id)
    except:
        return Http404('Статья не найдена')
    article.comment_set.create(comment_author=user, comment_text=request.POST['foo'])
    return HttpResponseRedirect(reverse('articles:article', args=(article.id,)))


def new_article_public(request):
    """Публикация новой статьи"""
    user = User.objects.get(pk=request.user.id)
    title = request.POST['title_article']
    text = request.POST['bar']
    poster = request.FILES['article_poster']
    Article.objects.create(article_author=user, article_title=title, article_text=text, article_poster=poster)
    return HttpResponseRedirect(reverse('articles:articles_page'))
