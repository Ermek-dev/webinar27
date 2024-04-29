from django.db import models
from django.db.models import TextChoices
from django.utils import timezone


class StatusChoice(TextChoices):
    ACTIVE = 'ACTIVE', 'Активна'
    NON_ACTIVE = 'NOT_ACTIVE','Неактивна'


class Article(models.Model):
    status = models.CharField(verbose_name='Статус', choices=StatusChoice.choices, max_length=20,
                              default=StatusChoice.ACTIVE)
    title = models.CharField(max_length=200, null = False, blank = False, verbose_name = 'Заголовок')
    text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
    author = models.CharField(max_length=200, null=False, blank=False, verbose_name='Автор')
    is_deleted = models.BooleanField(verbose_name='удалено',null=False,default=False)
    created_at = models.DateTimeField( auto_now_add=True,  verbose_name='Дата и время создания')
    updated_at = models.DateTimeField(auto_now=True,  verbose_name='Дата и время обновления')
    deleted_at = models.DateTimeField(verbose_name='Дата и время удаления',null=True,default=None)
    category = models.ForeignKey(
        verbose_name='Category',
        to='webapp.Category',
        null=True,
        blank = False,
        related_name='article',
        on_delete=models.RESTRICT
    )


    def __str__(self):
        return f'{self.author} - {self.title}'
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статья'


    def delete(self,using=None,keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=20,null=False, verbose_name='Категория')



    def __str__(self):
        return self.name





#
# class Comment(models.Model):
#     article = models.ForeignKey(
#         to='webapp.Article',
#         verbose_name='Статья',
#         null = False,
#         blank = False,
#         related_name = 'comments',
#         on_delete = models.RESTRICT
#
#     )
#
#     text = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Текст')
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
#     updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')


