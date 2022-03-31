import datetime
from django.contrib import messages
from django.shortcuts import redirect, render, get_object_or_404
from events.models import Event
from news.models import News
from .forms import ApplicationForm
from .models import (
    Subject, SchoolManagement, FrequentlyAskedQuestion,
    PTAManagement, Picture, PTAMeetingResolution, Tuition, About)


def home(request):
    now = datetime.datetime.now()
    events = Event.objects.filter(date__gte=now)[:3]
    next_event = None
    if events.exists():
        next_event = Event.objects.filter(date__gte=now).earliest()
    news = News.objects.all()[:3]
    tuitions = Tuition.objects.all()[:2]
    about = About.objects.first()
    context = {
        'events': events, 'next_event': next_event,
        'news': news, 'tuitions': tuitions,
        'about': about,
    }
    return render(request, 'home.html', context)


def application(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Application successfully sent.")
            return redirect(application)
        else:
            messages.warning(
                request, "There was an error, check below and resend.")
    else:
        form = ApplicationForm()
    return render(request, 'application.html', {'form': form})


def contact(request):
    return render(request, 'contact.html', {})


def curriculum(request):
    subjects = Subject.objects.all()
    return render(request, 'curriculum.html', {'subjects': subjects})


def faq(request):
    faqs = FrequentlyAskedQuestion.objects.all()
    return render(request, 'faq.html', {'faqs': faqs})


def gallery(request):
    pictures = Picture.objects.all()
    return render(request, 'gallery.html', {'pictures': pictures})


def history(request):
    return render(request, 'history.html', {})


def leadership_team(request):
    teams = SchoolManagement.objects.filter(role='L')
    return render(
        request, 'leadership_team.html', {'teams': teams})


def teachers(request):
    teams = SchoolManagement.objects.filter(role='T')
    return render(
        request, 'leadership_team.html', {'teams': teams})


def pta_management(request):
    teams = PTAManagement.objects.all()
    return render(request, 'pta_management.html', {'teams': teams})


def admission(request):
    return render(request, 'admission.html', {})


def resolutions(request):
    resolutions = PTAMeetingResolution.objects.all()
    return render(
        request, 'resolutions.html', {'resolutions': resolutions})


def resolution_detail(request, slug):
    resolution = get_object_or_404(PTAMeetingResolution, slug=slug)
    return render(
        request, 'resolution_detail.html', {'resolution': resolution})
