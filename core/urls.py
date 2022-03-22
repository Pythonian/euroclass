from django.urls import path
from . import views


urlpatterns = [
    path('application/', views.application, name='application'),
    path('contact/', views.contact, name='contact'),
    path('curriculum/', views.curriculum, name='curriculum'),
    path('faq/', views.faq, name='faq'),
    path('gallery/', views.gallery, name='gallery'),
    path('history/', views.history, name='history'),
    path('leadership_team/', views.leadership_team, name='leadership_team'),
    path('mission_vision/', views.mission_vision, name='mission_vision'),
    path('pta_management/', views.pta_management, name='pta_management'),
    path('admission/', views.admission, name='admission'),
    path('', views.home, name='home'),
]
