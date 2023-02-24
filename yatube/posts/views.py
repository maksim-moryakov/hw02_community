from .models import Group, Post

from django.shortcuts import render, get_object_or_404

from django.core.paginator import Paginator

POSTS_ON_PAGE: int = 10


def index(request):
    title = 'Последние обновления на сайте'
    posts = Post.objects.all()[:POSTS_ON_PAGE]
    paginator = Paginator(posts, POSTS_ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'title': title,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    title = 'Здесь будет информация о группах проекта Yatube'
    posts = group.posts.all()[:POSTS_ON_PAGE]
    paginator = Paginator(posts, POSTS_ON_PAGE)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'group': group,
        'title': title,
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)

