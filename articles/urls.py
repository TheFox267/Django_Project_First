from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='articles_page'),
    path('<int:article_id>', views.detail, name='article'),
    path('<int:article_id>/leave_comment/', views.leave_comment, name='leave_comment'),
    path('new_article/', views.new_article, name='new_article'),
    path('<int:article_id>/add_like/', views.add_like, name='add_like'),
    path('public_article/', views.new_article_public, name='new_article_public'),
]

#  Copyright (c) 2020.  Designed TheFox https://github.com/TheFox267
