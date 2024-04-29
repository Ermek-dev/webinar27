from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title','text','author','status','category')
        labels = {
            'title': 'Заголовок',
            'text': 'Текст',
            'author': 'Автор',
            'status': 'Статус',
            'category': 'Категория',
        }


    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длинее 2 символов')
        return title












# class ArticleForm(forms.ModelForm):
    # title = forms.CharField(max_length=100, required=True, label='Заголовок')
    # text = forms.CharField(max_length=3000, required=True, label = 'Текст',
    #                        widget=widgets.Textarea)
    # author = forms.CharField(max_length=50, required=True, label='Автор')


