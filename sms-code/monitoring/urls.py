


from django.urls import path

from .views import lobby, index


urlpatterns = [    

    path('lobby', lobby),
    
    path('', index)
]