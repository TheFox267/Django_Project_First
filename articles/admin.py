from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Article, Comment, ArticleStatistic, ArticleStatisticAdmin


# Register your models here.
class NewAdmin(SummernoteModelAdmin):
    summernote_fields = ('article_text', 'comment_text',)


admin.site.register(Article, NewAdmin)

admin.site.register(Comment, NewAdmin)

admin.site.register(ArticleStatistic, ArticleStatisticAdmin)

