from django import forms
from django_summernote.widgets import SummernoteWidget

from .models import Comment, Article


class CommentForm(forms.ModelForm):
    foo = forms.CharField(widget=SummernoteWidget(attrs={
        'summernote':
            {'width': '100%', 'height': '400px',
             'placeholder': 'Комментарий',
             'lazy': True,
             'lang': 'ru-Ru',
             'disableDragAndDrop': True,
             'disable_attachment': True,
             'fontNames': ['Verdana'],
             'disableGrammar': False,
             'fontNamesIgnoreCheck': ['Arial', 'Segoe UI', 'Arial', 'Comic Sans MS', 'Courier New', 'Segoe UI Emoji', 'Segoe UI Symbol'],
             'toolbar': [
                 ['stye', ['style']],
                 ['font', ['bold', 'underline', 'clear']],
                 ['fontname', ['fontname']],
                 ['color', ['color']],
                 ['para', ['ul', 'ol', 'paragraph']],
                 ['table', ['table']],
                 ['insert', ['link']],
                 ['view', ['fullscreen', 'codeview']]], }
    }
    ))

    class Meta:
        model = Comment
        fields = ['comment_text']


class ArticleForm(forms.ModelForm):
    bar = forms.CharField(widget=SummernoteWidget(attrs={
        'summernote':
            {'width': '100%', 'height': '400px',
                'placeholder': 'Статья',
                'lang': 'ru-Ru'

            }

    }
    ))

    class Meta:
        model = Article
        fields = ['article_text']

#  Copyright (c) 2020.  Designed TheFox https://github.com/TheFox267
