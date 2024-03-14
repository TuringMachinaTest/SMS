from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from braces.views import PermissionRequiredMixin
from django import forms

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

from django_filters.views import FilterView
from django_tables2 import LazyPaginator, SingleTableMixin, SingleTableView
from django_tables2.export.views import ExportMixin
from extra_views import CreateWithInlinesView, InlineFormSetFactory, ModelFormSetView, UpdateWithInlinesView
from view_breadcrumbs import DetailBreadcrumbMixin, ListBreadcrumbMixin, CreateBreadcrumbMixin

from .filters import AccountFilter, CityFilter, InstallationCompanyFilter

from .tables import AccountsTable, CityTable, InstallationCompanyTable

from .forms import AccountForm, AccountUserForm, AccountUserInlineFormSet, CityForm, InstallationCompanyForm
from .models import Account, AccountUser, City, InstallationCompany


class ListAccounts(PermissionRequiredMixin, ExportMixin, ListBreadcrumbMixin, SingleTableMixin, FilterView):
    
    permission_required = 'accounts.view_account'
    
    model = Account
    table_class = AccountsTable 
    paginator_class = LazyPaginator
    
    filterset_class = AccountFilter
    
    template_name = 'generic/list.html'
    
    crumbs = [
        ("Accounts", reverse_lazy('account_list'))
    ]
        
    def get_context_data(self, **kwargs):
        context = super(ListAccounts, self).get_context_data(**kwargs)
        
        context['add_url'] = reverse_lazy('account_create')
        context['export_url'] = reverse_lazy('account_list') + "?_export=csv"
        context['view_name'] = "Accounts"

        return context

class CreateAccount(PermissionRequiredMixin, CreateBreadcrumbMixin, CreateWithInlinesView):
        
    permission_required = 'accounts.add_account'
    
    model = Account
    form_class = AccountForm
    inlines = [AccountUserInlineFormSet]

    crumbs = [
        ("Accounts", reverse_lazy('account_list')),
        ("Create", reverse_lazy('account_create'))
    ]
    
    template_name = 'generic/details-create-update.html'
    success_url = reverse_lazy('account_list')

    def get_context_data(self, **kwargs):
        context = super(CreateAccount, self).get_context_data(**kwargs)

        context['view_name'] = "Create Account"

        return context

class DetailsAccount(PermissionRequiredMixin, DetailBreadcrumbMixin, UpdateWithInlinesView, DetailView):
        
    permission_required = 'accounts.view_account'
    
    
    
    model = Account
    form_class = AccountForm
    inlines = [AccountUserInlineFormSet]

    template_name = 'generic/details-create-update.html'
    
    def get_form_kwargs(self):
        # Get the default form kwargs
        kwargs = super().get_form_kwargs()
                
        # Add any additional parameters you want to pass to the form
        kwargs['details'] = True
        
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super(DetailsAccount, self).get_context_data(**kwargs)
        
        context['details'] = True
        
        return context
    
    def get_queryset(self):
        # Customize the queryset as needed (e.g., filter by user, etc.)
        return Account.objects.filter(pk=self.kwargs["pk"])


class UpdateeAccount(PermissionRequiredMixin, UpdateWithInlinesView):
    
    permission_required = 'accounts.view_account'
    
    model = Account
    form_class = AccountForm
    inlines = [AccountUserInlineFormSet]
    
    formset_kwargs = {'form_kwargs': {'test': False}}

    template_name = 'generic/details-create-update.html'
    success_url = reverse_lazy('account_list')
    
    def get_queryset(self):
        # Customize the queryset as needed (e.g., filter by user, etc.)
        return Account.objects.filter(pk=self.kwargs["pk"])
    
    
class DeleteAccount(PermissionRequiredMixin, DeleteView):
    
    permission_required = 'accounts.delete_account'
    
    model = Account
    template_name = 'generic/confirm-delete.html'

    success_url = reverse_lazy("account_list")
    
    
class ListInstallationCompanies(PermissionRequiredMixin, ExportMixin, SingleTableMixin, FilterView):
    
    permission_required = 'accounts.view_account'
    
    model = InstallationCompany
    table_class = InstallationCompanyTable 
    paginator_class = LazyPaginator
    
    filterset_class = InstallationCompanyFilter

    template_name = 'generic/list.html'
    

class CreatInstallationCompany(PermissionRequiredMixin, CreateWithInlinesView):
        
    permission_required = 'accounts.add_account'
    
    model = InstallationCompany
    form_class = InstallationCompanyForm

    template_name = 'generic/details-create-update.html'
    success_url = reverse_lazy('installation_company_list')


class UpdateeInstallationCompany(PermissionRequiredMixin, UpdateWithInlinesView):
    
    permission_required = 'accounts.view_account'
    
    model = InstallationCompany
    form_class = InstallationCompanyForm
    
    template_name = 'generic/details-create-update.html'
    success_url = reverse_lazy('installation_company_list')
    
    def get_queryset(self):
        # Customize the queryset as needed (e.g., filter by user, etc.)
        return InstallationCompany.objects.filter(pk=self.kwargs["pk"])
    
    
class DetailsInstallationCompany(PermissionRequiredMixin, UpdateWithInlinesView, DetailView):
    
    permission_required = 'accounts.view_account'
    
    model = InstallationCompany
    form_class = InstallationCompanyForm
    
    template_name = 'generic/details-create-update.html'
    
    def get_queryset(self):
        # Customize the queryset as needed (e.g., filter by user, etc.)
        return InstallationCompany.objects.filter(pk=self.kwargs["pk"])
    
    
class DeleteInstallationCompany(PermissionRequiredMixin, DeleteView):
    
    permission_required = 'accounts.delete_account'
    
    model = InstallationCompany
    template_name = 'generic/confirm-delete.html'

    success_url = reverse_lazy("installation_company_list")
    
    
class ListCities(PermissionRequiredMixin, ExportMixin, SingleTableMixin, FilterView):
    
    permission_required = 'accounts.view_account'
    
    model = City
    table_class = CityTable 
    paginator_class = LazyPaginator
    
    filterset_class = CityFilter

    template_name = 'generic/list.html'
    

class CreatCity(PermissionRequiredMixin, CreateWithInlinesView):
        
    permission_required = 'accounts.add_account'
    
    model = City
    form_class = CityForm

    template_name = 'generic/details-create-update.html'
    success_url = reverse_lazy('city_list')


class UpdateeCity(PermissionRequiredMixin, UpdateWithInlinesView):
    
    permission_required = 'accounts.view_account'
    
    model = City
    form_class = CityForm
    
    template_name = 'generic/details-create-update.html'
    success_url = reverse_lazy('city_list')
    
    def get_queryset(self):
        # Customize the queryset as needed (e.g., filter by user, etc.)
        return City.objects.filter(pk=self.kwargs["pk"])
    
    
class DeleteCity(PermissionRequiredMixin, DeleteView):
    
    permission_required = 'accounts.delete_account'
    
    model = City
    template_name = 'generic/confirm-delete.html'

    success_url = reverse_lazy("city_list")