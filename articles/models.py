import datetime

from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.

class Article(models.Model):
    objects = models.Manager()
    article_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор статьи')
    article_title = models.CharField('заголовок статьи', max_length=255)
    article_text = models.TextField('текст статьи')
    article_date = models.DateTimeField('дата публикации статьи', auto_now_add=True)
    article_poster = models.ImageField(upload_to='poster_image/%Y/%m/%d/')
    likes = models.ManyToManyField(User, related_name='likes', blank=True)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.article_title

    def was_published_recently(self):
        return self.article_date >= (timezone.now() - datetime.timedelta(days=1))

    def total_likes(self):
        return self.likes.count()


class ArticleStatistic(models.Model):
    class Meta:
        db_table = 'ArticleStatistic'

    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    date = models.DateField('дата', default=timezone.now)
    views = models.IntegerField('просмотры', default=0)

    def __str__(self):
        return self.article.article_title


class ArticleStatisticAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'date', 'views')
    search_fields = ('__str__',)


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор комментария')
    comment_text = models.CharField('текст комментария', max_length=255)

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
