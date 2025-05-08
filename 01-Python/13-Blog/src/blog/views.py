from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment

# Create your views here.

def index(request):
    last_article = Article.objects.latest('pub_date')
    articles_list = Article.objects.order_by("-pub_date")

    last_article.refresh_from_db()

    return render(request, "blog/index.html", {"last_article": last_article, "articles_list": articles_list})

def detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, "blog/detail.html", {"article": article})

def add_comment(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comment_content = request.POST.get('content')

    if comment_content:
        Comment.create_comment(article, comment_content)

        return render(request, 'blog/detail.html', {"article" : article})

def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    article = comment.article

    if request.method == "POST":

        new_content = request.POST.get('content')
        print("hello")

        if new_content:

            comment.content = new_content
            comment.save()

            return redirect(f'/blog/{article.id}/')

    return render(request, "blog/edit.html", {"comment":comment})

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    comment.delete()

    return redirect(f'/blog/{comment.article.id}/')
