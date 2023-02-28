from .models import Group, Post, User

from django.shortcuts import render, get_object_or_404, redirect

from django.core.paginator import Paginator

from django.contrib.auth.decorators import login_required

from .forms import PostForm

POSTS_ON_PAGE: int = 10


def paginator_object(request, post_list):
    paginator = Paginator(post_list, POSTS_ON_PAGE)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)


def index(request):
    title = 'Последние обновления на сайте'
    post_list = Post.objects.all()
    page_obj = paginator_object(request, post_list)
    context = {
        'title': title,
        'page_obj': page_obj,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    title = 'Здесь будет информация о группах проекта Yatube'
    post_list = group.posts.all()
    page_obj = paginator_object(request, post_list)
    context = {
        'group': group,
        'title': title,
        'page_obj': page_obj,
    }
    return render(request, 'posts/group_list.html', context)


def profile(request, username):
    user_author = get_object_or_404(User, username=username)
    post_list = user_author.posts.all()
    page_obj = paginator_object(request, post_list)
    context = {
        'page_obj': page_obj,
        'user_author': user_author
    }
    return render(request, 'posts/profile.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_number = Post.objects.select_related('author').filter(
        author=post.author).count()
    context = {
        'post': post,
        'post_number': post_number
    }
    return render(request, 'posts/post_detail.html', context)

@login_required
def post_create(request):
    form = PostForm(
        request.POST or None,
        files=request.FILES or None
    )
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:profile', post.author.username)
    context = {
        'form': form,
    }
    return render(request, 'posts/create_post.html', context)