from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm

def boards(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'website/boards.html', {'posts': posts})

def contents(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'website/contents.html', {'post': post})

def board_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('contents', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'website/board_new.html', {'form': form})
