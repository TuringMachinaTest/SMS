from django.urls import path, include
from rest_framework import routers

from events import views

router_v1 = routers.DefaultRouter()
router_v1.register(r'raw_events', views.EventViewSetV1)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('v1/events_management/', include(router_v1.urls)),
]

