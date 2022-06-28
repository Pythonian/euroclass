"""euroclass URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns = [
    path('webadmin/', admin.site.urls),
    path('news/', include('news.urls')),
    path('events/', include('events.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('favicon.ico',
         RedirectView.as_view(url=staticfiles_storage.url('favicon.ico'))),
    path('', include('core.urls')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
