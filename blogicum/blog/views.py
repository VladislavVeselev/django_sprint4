from .models import Post, Category
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.core.paginator import Paginator
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


User = get_user_model()


def index(request):
    posts = Post.objects.filter(
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    ).order_by('-pub_date')[:5]
    context = {'post_list': posts}
    return render(request, 'blog/index.html', context)



def post_detail(request, id):
    post = get_object_or_404(
        Post,
        id=id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True
    )
    context = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    posts = category.posts.filter(
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')
    context = {'category': category, 'post_list': posts}
    return render(request, 'blog/category.html', context)


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:profile', username=request.user.username)
    else:
        form = PostForm()

    return render(request, 'blog/create.html', {'form': form})


def profile(request, username):
    user = get_object_or_404(User, username=username)

    posts = user.posts.filter(
        is_published=True,
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')

    paginator = Paginator(posts, 10)  # 10 постов на страницу
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'profile': user,
        'page_obj': page_obj,  # 👈 ВАЖНО
    }
    return render(request, 'blog/profile.html', context)