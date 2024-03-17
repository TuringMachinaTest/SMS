from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def send_message(channel, type, message):
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        channel,
        {
            'type':type,
            'message': message
        }
    )