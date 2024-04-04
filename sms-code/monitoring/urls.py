


from django.urls import path

from .views import operator


urlpatterns = [        
    path('', operator, name='operator')
]