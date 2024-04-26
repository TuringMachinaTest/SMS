from django.shortcuts import render
from django.urls import reverse_lazy

from support.filters import ServiceOrderFilter
from support.forms import ServiceOrderForm
from support.models import ServiceOrder
from view_breadcrumbs import DetailBreadcrumbMixin, ListBreadcrumbMixin, CreateBreadcrumbMixin, UpdateBreadcrumbMixin, DeleteBreadcrumbMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.core import serializers

from django_filters.views import FilterView
from django_tables2 import LazyPaginator, SingleTableMixin, SingleTableView
from django_tables2.export.views import ExportMixin
from braces.views import PermissionRequiredMixin

from support.tables import ServiceOrderTable

from django.utils.translation import gettext as _


class ListServiceOrders(PermissionRequiredMixin, ExportMixin, ListBreadcrumbMixin, SingleTableMixin, FilterView):
    
    permission_required = 'accounts.view_account'
    
    model = ServiceOrder
    table_class = ServiceOrderTable 
    paginator_class = LazyPaginator
    
    filterset_class = ServiceOrderFilter

    template_name = 'generic/list.html'

    def get_context_data(self, **kwargs):
        context = super(ListServiceOrders, self).get_context_data(**kwargs)
        
        context['add_url'] = reverse_lazy('support:serviceorder_create')
        context['export_url'] = reverse_lazy('support:serviceorder_list') + "?_export=csv"
        context['view_name'] = _("Service Order")

        return context    


class CreateServiceOrder(PermissionRequiredMixin, CreateBreadcrumbMixin, CreateView):
        
    permission_required = 'accounts.add_account'
    
    model = ServiceOrder
    form_class = ServiceOrderForm

    template_name = 'generic/form.html'
    success_url = reverse_lazy('support:serviceorder_list')

    def get_context_data(self, **kwargs):
        context = super(CreateServiceOrder, self).get_context_data(**kwargs)
        
        context['view_name'] = _("Create Service Order")

        return context


class DetailsServiceOrder(PermissionRequiredMixin, DetailBreadcrumbMixin, UpdateView):
    
    permission_required = 'accounts.view_account'
    
    model = ServiceOrder
    form_class = ServiceOrderForm
    
    template_name = 'generic/form.html'

    def get_form_kwargs(self):
        # Get the default form kwargs
        kwargs = super().get_form_kwargs()
                
        # Add any additional parameters you want to pass to the form
        kwargs['details'] = True
        
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super(DetailsServiceOrder, self).get_context_data(**kwargs)
        
        context['details'] = True
        context['view_name'] = _("Service Order Details")

        return context
        
    def get_queryset(self):
        # Customize the queryset as needed (e.g., filter by user, etc.)
        return ServiceOrder.objects.filter(pk=self.kwargs["pk"])
    

class UpdateeServiceOrder(PermissionRequiredMixin, UpdateBreadcrumbMixin, UpdateView):
    
    permission_required = 'accounts.view_account'
    
    model = ServiceOrder
    form_class = ServiceOrderForm
    
    template_name = 'generic/form.html'
    success_url = reverse_lazy('support:serviceorder_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateeServiceOrder, self).get_context_data(**kwargs)

        instance = self.get_queryset().first()

        context['view_name'] = _("Update Service Order")
        context['history'] = serializers.serialize("python", instance.history.all())

        return context
    
    def get_queryset(self):
        # Customize the queryset as needed (e.g., filter by user, etc.)
        return ServiceOrder.objects.filter(pk=self.kwargs["pk"])
    
    
class DeleteServiceOrder(PermissionRequiredMixin, DeleteBreadcrumbMixin, DeleteView):
    
    permission_required = 'accounts.delete_account'
    
    model = ServiceOrder
    template_name = 'generic/confirm_delete.html'

    success_url = reverse_lazy("support:serviceorder_list")
    