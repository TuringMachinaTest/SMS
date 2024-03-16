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