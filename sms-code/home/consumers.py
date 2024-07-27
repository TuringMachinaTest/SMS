import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync


class AlertConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'alerts'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()
   

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        
    
    def send_event_alert(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'send_event_alert',
            'message':message
        }))