from django.urls import path

from . import views

urlpatterns = [
    path('<slug:slug>/', views.news_detail, name='news_detail'),
    path('', views.news, name='news'),
]
