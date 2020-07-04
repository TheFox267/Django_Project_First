from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from articles.models import Article


# Create your views here.
def visible(request, user_id):
    """Отобразить профиль редактирования пользователя"""
    user = User.objects.get(id=user_id)
    current_article = Article.objects.filter(article_author=request.user)
    return render(request, 'userprofile/profile_edit.html', {'user': user, 'article_list': current_article, 'current_user': request.user.id})


def visible_user_page(request, user_id):
    """Отобразить профиль пользователя с его информацией для всех пользователей"""
    user = User.objects.get(id=user_id)
    current_article = Article.objects.filter(article_author=user_id)
    liked_article = Article.objects.filter(likes=user.id)

    return render(request, 'userprofile/profile_user_page.html', {'user': user, 'current_article': current_article, 'current_user': request.user.id, 'liked_article': liked_article})


def update_info(request, user_id):
    """Обновить информацию в профиле"""
    user = User.objects.get(id=user_id)
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.profile.gender_choice = request.POST['gender']
    user.profile.bio = request.POST['bio']
    user.profile.birth_date = request.POST['date_br']
    try:
        user.profile.avatar = request.FILES['avatar_user']
    except:
        user.profile.avatar = user.profile.avatar
    user.save()
    return HttpResponseRedirect(reverse('userprofile:profile_page', args=(user_id,)))
