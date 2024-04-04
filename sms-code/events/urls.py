


from django.urls import path

from .views import ListRawEvents, CreateDecryptedEvent, UpdateDecryptedEvent, DetailsDecryptedEvent, ListDecryptedEvents


urlpatterns = [
    path('raw_events/list', ListRawEvents.as_view(), name='rawevent_list'),
    path('raw_events/view/<int:pk>', ListRawEvents.as_view(), name='rawevent_detail'),
    
    path('decrypted_events/list', ListDecryptedEvents.as_view(), name='decryptedevent_list'),
    path('decrypted_events/create', CreateDecryptedEvent.as_view(), name='decryptedevent_create'),
    path('decrypted_events/update/<int:pk>', UpdateDecryptedEvent.as_view(), name='decryptedevent_update'),
    path('decrypted_events/view/<int:pk>', DetailsDecryptedEvent.as_view(), name='decryptedevent_detail'),

]