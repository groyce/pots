from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import Event
from django.utils import timezone


def EventsPage(request):
    now = timezone.now()
    events = Event.objects.all()
    return render(request, 'events/events.html', {'events': events.reverse()})


def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'events/event_detail.html', {'event': event, })
