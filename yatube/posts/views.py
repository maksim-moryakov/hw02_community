from .models import Group, Post 

from django.shortcuts import render, get_object_or_404

POSTS_ON_PAGE: int = 10

def index(request):
    template = 'posts/index.html'
    title = 'Последние обновления на сайте'
    posts = Post.objects.all()[:POSTS_ON_PAGE]
    context = {
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    posts = group.posts.all()[:POSTS_ON_PAGE]
    context = {
        'group': group,
        'title': title,
        'posts': posts,
    }
    return render(request, template, context)
