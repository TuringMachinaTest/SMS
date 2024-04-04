from django.urls import path

from .views import ListDevices, DetailsDevice, CreateDevice, UpdateeDevice, DeleteDevice


urlpatterns = [
    path('devices/list', ListDevices.as_view(), name='device_list'),
    path('devices/details/<int:pk>', DetailsDevice.as_view(), name='device_detail'),
    path('devices/create/', CreateDevice.as_view(), name='device_create'),
    path('devices/update/<int:pk>', UpdateeDevice.as_view(), name='device_update'),
    path('devices/view/<int:pk>', DeleteDevice.as_view(), name='device_delete'),
    
    path('devices/list', ListDevices.as_view(), name='decryption_configurations'),
]