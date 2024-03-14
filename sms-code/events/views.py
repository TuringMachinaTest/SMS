from django.shortcuts import render
from django.urls import reverse_lazy
from django_tables2 import LazyPaginator, SingleTableMixin
from view_breadcrumbs import BaseBreadcrumbMixin, ListBreadcrumbMixin
from django_tables2.export.views import ExportMixin
from django_tables2 import LazyPaginator, SingleTableMixin, SingleTableView
from django_filters.views import FilterView
from braces.views import PermissionRequiredMixin

from .models import RawEvent

from .tables import RawEventTable

from .filter import RawEventFilter

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