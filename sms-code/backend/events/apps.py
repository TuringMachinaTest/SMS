from django.apps import AppConfig


class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'events'

 #   def ready(self):
 #       devices = Device.objects.all()
 #       for device in devices:
 #           redis_client.lock(device.name).release()
