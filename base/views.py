from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from django.core.serializers import json
from base.models import Rental
from base.forms import RentalForm
import json

# Create your views here.

def index(request):
    context = {}
    return render(request, 'base/index.html', context)

def getEvents(request):
    events = Rental.objects.all().values('title', 'start', 'end')
    e_list = []
    for event in list(events):
        e_list.append(event)
    events_json = json.dumps(e_list, default=str)

    return HttpResponse(events_json, content_type='application/json')

def createRent(request):
    form = RentalForm
    context = {'form': form}

    return render(request, 'base/rental_form.html', context)