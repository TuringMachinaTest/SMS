from django.urls import path

from support.views import CreateServiceOrder, DeleteServiceOrder, DetailsServiceOrder, ListServiceOrders, UpdateeServiceOrder


urlpatterns = [
    path('service_orders/list', ListServiceOrders.as_view(), name='serviceorder_list'),
    path('service_orders/details/<int:pk>', DetailsServiceOrder.as_view(), name='serviceorder_detail'),
    path('service_orders/create/', CreateServiceOrder.as_view(), name='serviceorder_create'),
    path('service_orders/update/<int:pk>', UpdateeServiceOrder.as_view(), name='serviceorder_update'),
    path('service_orders/view/<int:pk>', DeleteServiceOrder.as_view(), name='serviceorder_delete'),
]