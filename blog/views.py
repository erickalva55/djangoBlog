from django.http.response import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render

from content.models import Post


def welcome(request):
    posts = Post.objects.filter(status=Post.ACTIVE)

    return render(request, 'blog/index.html', {'posts': posts})


def about(request):
    return render(request, 'blog/about.html')


def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")
