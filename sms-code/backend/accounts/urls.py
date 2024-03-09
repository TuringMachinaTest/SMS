from django.urls import path, include
from rest_framework import routers

from accounts import views

router_v1 = routers.DefaultRouter()
router_v1.register(r'cities', views.CityViewSetV1)
router_v1.register(r'accounts', views.AccountViewSetV1)
router_v1.register(r'account_users', views.AccountUserViewSetV1)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('v1/accounts_management/', include(router_v1.urls)),
]

