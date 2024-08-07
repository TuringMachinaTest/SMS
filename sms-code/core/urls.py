"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from core import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [    
    path('accounts-management/', include(('accounts.urls', 'accounts'), namespace="accounts")),
    path('events-management/', include(('events.urls', 'events'), namespace="events")),
    path('configurations/', include(('configurations.urls', 'configurations'), namespace="configurations")),
    path('support/', include(('support.urls', 'support'), namespace="support")),

    path("", include(('monitoring.urls', 'monitoring'), namespace="monitoring")),
    
    path("admin/", admin.site.urls),
    
    path("select2/", include("django_select2.urls")),
    #path('report_builder/', include('report_builder_scheduled.urls')),
    path('report_builder/', include('report_builder.urls')),
    
    path("", include('admin_adminlte.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
