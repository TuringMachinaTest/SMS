


from django.urls import path

from .views import ListRawEvents


urlpatterns = [
    path('raw_events/list', ListRawEvents.as_view(), name='rawevent_list'),
]