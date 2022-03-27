from news.models import News
from .models import About, SchoolContactInfo


def euroclass(request):
    return {
        'about': About.objects.first(),
        'latest_news': News.objects.all()[:3],
        'info': SchoolContactInfo.objects.first(),
    }
