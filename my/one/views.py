from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by("published_date")
    return render(request, "one/post_list.html", {'post': posts})


def post_d(request, aza):
    post = get_object_or_404(Post, pk=aza)
    return render(request, "one/post_detail.html", {"po": post})

