from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.forms.models import model_to_dict
from django.core import serializers

from events.models import DecryptedEvent, RawEvent
from events.serializers import DecryptedEventSerializer, RawEventSerializer


# Create your views here.

def lobby(request):
    return render(request, 'events/lobby.html')

# For each album object, tracks should be fetched from database
#print(AlbumSerializer(qs, many=True).data)


def index(request):
    
    uncommited_events = DecryptedEvent.objects.filter(status=0).order_by('id')
    uncommited_events = DecryptedEventSerializer(uncommited_events, many=True).data
    
    follow_events = DecryptedEvent.objects.filter(status=3).order_by('id')
    follow_events = DecryptedEventSerializer(follow_events, many=True).data
    
    pending_events = DecryptedEvent.objects.filter(status=2).order_by('id')
    pending_events = DecryptedEventSerializer(pending_events, many=True).data
    
    locked_events = DecryptedEvent.objects.filter(status=-1).order_by('id')
    locked_events = DecryptedEventSerializer(locked_events, many=True).data
    
    return render(request, 'monitoring/index.html', 
                {
                    'uncommited_events': json.dumps(uncommited_events),
                    'follow_events': json.dumps(follow_events),
                    'pending_events': json.dumps(pending_events),
                    'locked_events': json.dumps(locked_events),
                }
            )