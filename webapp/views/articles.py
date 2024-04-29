from django.core.handlers.wsgi import WSGIRequest
from django.http.response import HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from webapp.forms import ArticleForm
from webapp.models import Article, StatusChoice

def add_view(request: WSGIRequest):
    if request.method == 'GET':
        form = ArticleForm()
        return render(request, 'article_create.html',context={'choices': StatusChoice.choices,'form': form})
    #Post
    form = ArticleForm(data=request.POST)
    print(form.__dict__)
    if not form.is_valid():
        return render(request,
                      'article_create.html',
                      context={
                          'choices': StatusChoice.choices,
                          'form': form
                      })
    #Success
    else:
        article = Article.objects.create(**form.cleaned_data)
        return redirect('article_detail',pk=article.pk)


def detail_view(request,pk):
    article = get_object_or_404(Article,pk=pk)
    return render(request, 'article.html', context ={
       'article': article
    })


def update_view(request, pk):
    article = get_object_or_404(Article,pk=pk)

    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail',pk=article.pk)
        return render(request, 'article_update.html', context={'form': form, 'article':article})
    form = ArticleForm(instance=article)
    return render(request,'article_update.html',context={'form':form, 'article':article })



























#
# def update_view(request, pk):
#     article = get_object_or_404(Article,pk=pk)
#     if request.method == 'POST':
#         article.title = request.POST.get('title')
#         article.author = request.POST.get('author')
#         article.text = request.POST.get('text')
#         article.status = request.POST.get('status')
#         article.save()
#         return redirect('article_detail',pk=article.pk)
#     return render(request, 'article_update.html',
#                   context={
#                   'article':article,
#                   'choices': StatusChoice.choices
#     })
#


def delete_view(request,pk):
    article = get_object_or_404(Article,pk=pk)
    return render(request,'article_confirm_delete.html',context={
        'article': article
    })


def confirm_delete(request,pk):
    article = get_object_or_404(Article,pk=pk)
    article.delete()
    return redirect('index')






# { % if errors %}
# < p
#
#
# class ="error" > {{errors.title}} < / p >
#
#
# { % endif %}
#
# def update_view(request, pk):
#     errors = {}
#     article = get_object_or_404(Article,pk=pk)
#     if request.method == 'POST':
#         if not request.POST.get('title'):
#             errors['title'] = 'Данное поле обязательно к заполнению'
#         article.title = request.POST.get('title')
#         article.author = request.POST.get('author')
#         article.text = request.POST.get('text')
#         article.status = request.POST.get('status')
#         if errors:
#             return render(request, 'article_update.html',
#                           context={
#                               'article': article,
#                               'choices': StatusChoice.choices,
#                               'errors' : errors
#                           })
#
#         article.save()
#         return redirect('article_detail',pk=article.pk)
#     return render(request, 'article_update.html',
#                   context={
#                   'article':article,
#                   'choices': StatusChoice.choices
#     })





#
#
# def add_view(request: WSGIRequest):
#     if request.method == 'GET':
#         return render(request,'article_create.html')
#     print(request.POST)
#     context = {
#         'title': request.POST.get('title'),
#         'text': request.POST.get('text'),
#         'author': request.POST.get('author'),
#     }
#     return render(request, 'article.html',context=context)




# def add_view(request: WSGIRequest):
#     if request.method == 'GET':
#         return render(request,'article_create.html',context={
#             'choices': StatusChoice.choices
#         })
#     article_data = {
#         'title': request.POST.get('title'),
#         'text': request.POST.get('text'),
#         'author': request.POST.get('author'),
#     }
#     article = Article.objects.create(**article_data)
#     return redirect('article_detail',pk=article.pk)

