from django.urls import path
from . import views


urlpatterns = [
    path('application/', views.application, name='application'),
    path('tuitions/', views.tuitions, name='tuitions'),
    path('contact/', views.contact, name='contact'),
    path('curriculum/', views.curriculum, name='curriculum'),
    path('faq/', views.faq, name='faq'),
    path('gallery/', views.gallery, name='gallery'),
    path('history/', views.history, name='history'),
    path('leadership_team/', views.leadership_team, name='leadership_team'),
    path('teachers/', views.teachers, name='teachers'),
    path('pta_management/', views.pta_management, name='pta_management'),
    path('admission/', views.admission, name='admission'),
    path('resolutions/<slug:slug>/',
         views.resolution_detail, name='resolution'),
    path('resolutions/', views.resolutions, name='resolutions'),
    path('', views.home, name='home'),
]
