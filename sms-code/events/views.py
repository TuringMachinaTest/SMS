from datetime import datetime
from django.urls import reverse_lazy
from django_tables2 import LazyPaginator, SingleTableMixin
from django.views.generic.edit import CreateView, UpdateView
from view_breadcrumbs import CreateBreadcrumbMixin, DetailBreadcrumbMixin, ListBreadcrumbMixin, UpdateBreadcrumbMixin
from django_tables2.export.views import ExportMixin
from django_tables2 import LazyPaginator, SingleTableMixin, SingleTableView
from django_filters.views import FilterView
from braces.views import PermissionRequiredMixin
from django.core import serializers

from events.forms import DecryptedEventForm
from events.serializers import DecryptedEventSerializer

from .models import DecryptedEvent, RawEvent

from .tables import DecryptedEventTable, RawEventTable

from .filter import DecryptedEventFilter, RawEventFilter

from django.utils.translation import gettext as _
class ListRawEvents(PermissionRequiredMixin, ExportMixin, ListBreadcrumbMixin, SingleTableMixin, FilterView):
    
    permission_required = 'accounts.view_account'
    
    model = RawEvent
    table_class = RawEventTable 
    paginator_class = LazyPaginator

    filterset_class = RawEventFilter

    template_name = 'generic/list.html'

    def get_context_data(self, **kwargs):
        context = super(ListRawEvents, self).get_context_data(**kwargs)
        
        context['export_url'] = reverse_lazy('events:rawevent_list') + "?_export=csv"
        context['view_name'] = _("Raw Events")

        return context   


class ListDecryptedEvents(PermissionRequiredMixin, ExportMixin, ListBreadcrumbMixin, SingleTableMixin, FilterView):
    
    permission_required = 'accounts.view_account'
    
    model = DecryptedEvent
    table_class = DecryptedEventTable 
    paginator_class = LazyPaginator

    filterset_class = DecryptedEventFilter

    template_name = 'generic/list.html'

    def get_context_data(self, **kwargs):
        context = super(ListDecryptedEvents, self).get_context_data(**kwargs)
        
        context['export_url'] = reverse_lazy('events:decryptedevent_list') + "?_export=csv"
        context['view_name'] = _("Raw Events")

        return context 
    
    
class CreateDecryptedEvent(PermissionRequiredMixin, CreateBreadcrumbMixin, CreateView):
        
    permission_required = 'accounts.add_account'
    
    model = DecryptedEvent
    form_class = DecryptedEventForm

    template_name = 'generic/form.html'
    success_url = reverse_lazy('events:decryptedevent_list')

    def get_context_data(self, **kwargs):
        context = super(CreateDecryptedEvent, self).get_context_data(**kwargs)
        
        context['view_name'] = _("Create Custom Event")
        context['history'] = self.get_queryset().first().history.all()

        return context
   
   
class DetailsDecryptedEvent(PermissionRequiredMixin, DetailBreadcrumbMixin, UpdateView):
    
    permission_required = 'accounts.view_account'
    
    model = DecryptedEvent
    form_class = DecryptedEventForm
    
    template_name = 'generic/form.html'

    def get_form_kwargs(self):
        # Get the default form kwargs
        kwargs = super().get_form_kwargs()
                
        # Add any additional parameters you want to pass to the form
        kwargs['details'] = True
        
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super(DetailsDecryptedEvent, self).get_context_data(**kwargs)
        
        context['details'] = True
        context['view_name'] = _("View Event")
        context['history'] = serializers.serialize("python", self.get_queryset().first().history.all())

        return context
        
    def get_queryset(self):
        # Customize the queryset as needed (e.g., filter by user, etc.)
        return DecryptedEvent.objects.filter(pk=self.kwargs["pk"])
    
    
class UpdateDecryptedEvent(PermissionRequiredMixin, UpdateBreadcrumbMixin, UpdateView):
    
    permission_required = 'accounts.view_account'
    
    model = DecryptedEvent
    form_class = DecryptedEventForm
    
    template_name = 'generic/form.html'
    
    success_url = reverse_lazy('monitoring:operator')
    
    def get_form_kwargs(self):
        # Get the default form kwargs
        kwargs = super().get_form_kwargs()
        
        instance = self.get_queryset().first()
        if instance.status == -1 and (instance.locked_by == None or instance.locked_by != self.request.user.id) and not self.request.user.is_superuser:
            kwargs['details'] = True        
        # Add any additional parameters you want to pass to the form
        
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super(UpdateDecryptedEvent, self).get_context_data(**kwargs)
        
        instance = self.get_queryset().first()
        if instance.status != -1:
            instance.status = -1
            instance.locked_at = datetime.now()
            instance.locked_by = self.request.user
            instance.save()
        elif instance.locked_by == None or instance.locked_by != self.request.user.id:
            context['details'] = True

        context['view_name'] = _("Update Event")
        context['history'] = serializers.serialize("python", instance.history.all())
        self.success_url = self.request.META.get('HTTP_REFERER')

        return context
    
    def get_queryset(self):
        # Customize the queryset as needed (e.g., filter by user, etc.)
        return DecryptedEvent.objects.filter(pk=self.kwargs["pk"])
        
