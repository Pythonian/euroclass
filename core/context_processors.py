from news.models import News
from .models import FrequentlyAskedQuestion, Legal, About


def euroclass(request):
    return {
        'legal': Legal.objects.first(),
        'about': About.objects.first(),
        'latest_news': News.objects.all()[:3]
    }
