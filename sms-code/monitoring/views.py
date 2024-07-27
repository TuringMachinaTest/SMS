from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
import json
from django.forms.models import model_to_dict
from django.core import serializers

from events.models import DecryptedEvent, RawEvent
from events.serializers import DecryptedEventSerializer, RawEventSerializer

@login_required
def operator(request):
    
    uncommited_events = DecryptedEvent.objects.filter(status=0).order_by('-alarm_code__priority')
    uncommited_events = DecryptedEventSerializer(uncommited_events, many=True).data
    
    follow_events = DecryptedEvent.objects.filter(status=3).order_by('-alarm_code__priority')
    follow_events = DecryptedEventSerializer(follow_events, many=True).data
    
    pending_events = DecryptedEvent.objects.filter(status=2).order_by('-alarm_code__priority')
    pending_events = DecryptedEventSerializer(pending_events, many=True).data
    
    locked_events = DecryptedEvent.objects.filter(status=-1).order_by('-alarm_code__priority')
    locked_events = DecryptedEventSerializer(locked_events, many=True).data
    
    delayed_events = DecryptedEvent.objects.filter(status=4).order_by('-alarm_code__priority')
    delayed_events = DecryptedEventSerializer(delayed_events, many=True).data
    
    delayed_periodic_events = DecryptedEvent.objects.filter(status=5).order_by('-alarm_code__priority')
    delayed_periodic_events = DecryptedEventSerializer(delayed_periodic_events, many=True).data
    
    return render(request, 'monitoring/index.html', 
                {
                    'uncommited_events': json.dumps(uncommited_events),
                    'follow_events': json.dumps(follow_events),
                    'pending_events': json.dumps(pending_events),
                    'locked_events': json.dumps(locked_events),
                    'delayed_events': json.dumps(delayed_events),
                    'delayed_periodic_events': json.dumps(delayed_periodic_events)
                }
            )