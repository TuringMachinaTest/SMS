import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class EventConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'events'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
   

    def receive(self, text_data):
        text_data_json = json.loads(text_data)


    def send_raw_event(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'raw_event',
            'message':message
        }))
        
    def send_uncommited_event(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'uncommited_event',
            'message':message
        }))
    
    def remove_uncommited_event(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'remove_uncommited_event',
            'message':message
        }))
        
    def send_lock_event(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'lock_event',
            'message':message
        }))
        
    def remove_lock_event(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'remove_lock_event',
            'message':message
        }))
        
    def send_pending_event(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'pending_event',
            'message':message
        }))
        
    def remove_pending_event(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'remove_pending_event',
            'message':message
        }))
        
    def send_follow_event(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'follow_event',
            'message':message
        }))
        
    def remove_follow_event(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'remove_follow_event',
            'message':message
        }))
        
    def send_delayed_event(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'delayed_event',
            'message':message
        }))

    def remove_delayed_event(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'remove_delayed_event',
            'message':message
        }))
                
    def send_delayed_periodic_event(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'delayed_periodic_event',
            'message':message
        }))
        
    def remove_delayed_periodic_event(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'remove_delayed_periodic_event',
            'message':message
        }))