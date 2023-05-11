from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArticleForm
from .models import Article, Comment, Like
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def new(request):
    form = ArticleForm()

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)

        if form.is_valid():
            article = form.save(
                commit=False
            )
            article.author = request.user
            article.save()
            return redirect('article:detail', id=article.id)

    return render(request, 'new.html', {'form': form})

def detail(request, id):
    article = get_object_or_404(Article, pk=id)
    comments = Comment.objects.filter(article=article)
    like_count = len(Like.objects.filter(article=article))

    return render(request, 'detail.html', {'article': article, 'comments': comments, 'like_count':like_count})


def edit(request, id):
    article = get_object_or_404(Article, pk=id)

    form = ArticleForm(instance=article)

    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES,instance=article)

        if form.is_valid():
            article = form.save()
            return redirect('article:detail', id = article.id)

    return render(request, 'edit.html', {'form':form, 'article':article})


def destroy(request, id):
    article = get_object_or_404(Article, pk=id)

    article.delete()

    return redirect('main:index')

def create_comment(request, id):
    comment=Comment()
    comment.content = request.POST.get('content')
    comment.article = get_object_or_404(Article, pk=id)
    comment.author = request.user
    comment.save()
    return redirect('article:detail', id = id)

def new_comment(request, id):
    article = get_object_or_404(Article, pk=id)
    return render(request, 'new_comment.html', {'article': article})

def like(request, id):
    article = get_object_or_404(Article, pk=id)

    if request.user.is_anonymous:
        return redirect('user:signin')
    

    else:
        like_check=Like.objects.filter(like_users=request.user, article=article)
        if like_check:
            like_check.delete()
            return redirect('article:detail', id)
        # 좋아요 추가 
        else:
            like = Like()
            like.article = get_object_or_404(Article, pk=id)
            like.like_users = request.user
            like.save()
            return redirect('article:detail', id)
 
@login_required        
def commentlike(request, id):
    comment = get_object_or_404(Comment, pk=id)
    if request.user == comment.author:
        messages.error(request,'본인이 작성한 댓글은 추천할 수 없습니다.')
        
    else:
        comment.like_user_comment.add(request.user)
    return redirect('article:detail', id=comment.article.id)
