from django.shortcuts import render, get_object_or_404

from .models import News


def news(request):
    news = News.objects.all()
    return render(request, 'news.html', {'news': news})


def news_detail(request, slug):
    news = get_object_or_404(News, slug=slug)
    return render(request, 'news_detail.html', {'news': news})
