from django.shortcuts import render, get_object_or_404
import datetime
from .models import Event


def events(request):
    now = datetime.datetime.now()
    events = Event.objects.filter(date__gte=now)
    next_event = None
    if events.exists():
        next_event = Event.objects.filter(date__gte=now).earliest()
    return render(
        request, 'events.html',
        {'events': events, 'next_event': next_event})


def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'event_detail.html', {'event': event})
