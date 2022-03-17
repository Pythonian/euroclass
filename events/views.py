from django.shortcuts import render, get_object_or_404

from .models import Event


def events(request):
    events = Event.objects.all()  # dont dispaly past events
    next_event = Event.objects.latest()
    return render(
        request, 'events.html',
        {'events': events, 'event': next_event})


def event_detail(request, slug):
    event = get_object_or_404(Event, slug=slug)
    return render(request, 'event_detail.html', {'event': event})
