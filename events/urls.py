from django.urls import path

from . import views

urlpatterns = [
    path('<slug:slug>/', views.event_detail, name='event_detail'),
    path('', views.events, name='events'),
]
