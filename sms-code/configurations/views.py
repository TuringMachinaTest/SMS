from django.urls import reverse_lazy
from django_tables2 import LazyPaginator, SingleTableMixin
from extra_views import CreateWithInlinesView
from view_breadcrumbs import BaseBreadcrumbMixin, CreateBreadcrumbMixin, DeleteBreadcrumbMixin, DetailBreadcrumbMixin, ListBreadcrumbMixin, UpdateBreadcrumbMixin
from django_tables2.export.views import ExportMixin
from django_tables2 import LazyPaginator, SingleTableMixin, SingleTableView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from braces.views import PermissionRequiredMixin

from .forms import DeviceForm

from .models import Device

from .tables import DeviceTable

from django.utils.translation import gettext as _


class ListDevices(PermissionRequiredMixin, ExportMixin, ListBreadcrumbMixin, SingleTableMixin, ListView):
    
    permission_required = 'configurations.view_device'
    
    model = Device
    table_class = DeviceTable 
    paginator_class = LazyPaginator

    template_name = 'generic/list.html'

    def get_context_data(self, **kwargs):
        context = super(ListDevices, self).get_context_data(**kwargs)
        
        context['export_url'] = reverse_lazy('configurations:device_list') + "?_export=csv"
        context['add_url'] = reverse_lazy('configurations:device_create')
        context['view_name'] = _("Raw Events")

        return context   
    

class CreateDevice(PermissionRequiredMixin, CreateBreadcrumbMixin, CreateView):
        
    permission_required = 'configurations.add_device'
    
    model = Device
    form_class = DeviceForm

    template_name = 'generic/form.html'
    success_url = reverse_lazy('configurations:device_list')

    def get_context_data(self, **kwargs):
        context = super(CreateDevice, self).get_context_data(**kwargs)
        
        context['view_name'] = _("Create Device")

        return context


class DetailsDevice(PermissionRequiredMixin, DetailBreadcrumbMixin, DetailView):
    
    permission_required = 'configurations.view_device'
    
    model = Device
    form_class = DeviceForm
    
    template_name = 'generic/form.html'

    def get_form_kwargs(self):
        # Get the default form kwargs
        kwargs = super().get_form_kwargs()
                
        # Add any additional parameters you want to pass to the form
        kwargs['details'] = True
        
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super(DetailsDevice, self).get_context_data(**kwargs)
        
        context['details'] = True
        context['view_name'] = _("Device Details")

        return context
        
    def get_queryset(self):
        # Customize the queryset as needed (e.g., filter by user, etc.)
        return Device.objects.filter(pk=self.kwargs["pk"])
    

class UpdateeDevice(PermissionRequiredMixin, UpdateBreadcrumbMixin, UpdateView):
    
    permission_required = 'configurations.change_device'
    
    model = Device
    form_class = DeviceForm
    
    template_name = 'generic/form.html'
    success_url = reverse_lazy('configurations:device_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateeDevice, self).get_context_data(**kwargs)
        
        context['view_name'] = _("Update Device")

        return context
    
    def get_queryset(self):
        # Customize the queryset as needed (e.g., filter by user, etc.)
        return Device.objects.filter(pk=self.kwargs["pk"])
    
    
class DeleteDevice(PermissionRequiredMixin, DeleteBreadcrumbMixin, DeleteView):
    
    permission_required = 'configurations.delete_device'
    
    model = Device
    template_name = 'generic/confirm_delete.html'

    success_url = reverse_lazy("device_list")