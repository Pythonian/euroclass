from django.shortcuts import render


def home(request):
    return render(request, 'home.html', {})


def application(request):
    return render(request, 'application.html', {})


def contact(request):
    return render(request, 'contact.html', {})


def curriculum(request):
    return render(request, 'curriculum.html', {})


def faq(request):
    return render(request, 'faq.html', {})


def gallery(request):
    return render(request, 'gallery.html', {})


def history(request):
    return render(request, 'history.html', {})


def leadership_team(request):
    return render(request, 'leadership_team.html', {})


def mission_vision(request):
    return render(request, 'mission_vision.html', {})


def privacy(request):
    return render(request, 'privacy.html', {})


def pta_management(request):
    return render(request, 'pta_management.html', {})


def terms(request):
    return render(request, 'terms.html', {})
