from django.shortcuts import render

from .models import Subject, SchoolManagement, FrequentlyAskedQuestion


def home(request):
    return render(request, 'home.html', {})


def application(request):
    return render(request, 'application.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def curriculum(request):
    subjects = Subject.objects.all()
    return render(request, 'curriculum.html', {'subjects': subjects})


def faq(request):
    faqs = FrequentlyAskedQuestion.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})


def gallery(request):
    return render(request, 'gallery.html', {})


def history(request):
    return render(request, 'history.html', {})


def leadership_team(request):
    teams = SchoolManagement.objects.all()
    return render(
        request, 'leadership_team.html', {'teams': teams})


def mission_vision(request):
    return render(request, 'mission_vision.html', {})


def pta_management(request):
    return render(request, 'pta_management.html', {})


def admission(request):
    return render(request, 'admission.html', {})
