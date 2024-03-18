import json
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from braces.views import PermissionRequiredMixin
from django.core import serializers

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView

from django_filters.views import FilterView
from django_tables2 import LazyPaginator, SingleTableMixin, SingleTableView
from django_tables2.export.views import ExportMixin
from extra_views import CreateWithInlinesView, InlineFormSetFactory, ModelFormSetView, UpdateWithInlinesView
from view_breadcrumbs import DetailBreadcrumbMixin, ListBreadcrumbMixin, CreateBreadcrumbMixin, UpdateBreadcrumbMixin, DeleteBreadcrumbMixin

from configurations.forms import AlarmCodeInlineFormSet

from .filters import AccountFilter, CityFilter, GroupFilter, InstallationCompanyFilter

from .tables import AccountsTable, CityTable, GroupTable, InstallationCompanyTable

from .forms import AccountForm, AccountUserForm, AccountUserInlineFormSet, CityForm, GroupForm, InstallationCompanyForm, ZoneInlineFormSet
from .models import Account, AccountUser, City, Group, InstallationCompany

from django.utils.translation import gettext as _

class ListAccounts(PermissionRequiredMixin, ExportMixin, ListBreadcrumbMixin, SingleTableMixin, FilterView):
    
    permission_required = 'accounts.view_account'
    
    model = Account
    table_class = AccountsTable 
    paginator_class = LazyPaginator
    
    filterset_class = AccountFilter
    
    template_name = 'generic/list.html'

    def get_context_data(self, **kwargs):
        context = super(ListAccounts, self).get_context_data(**kwargs)
        
        context['add_url'] = reverse_lazy('accounts:account_create')
        context['export_url'] = reverse_lazy('accounts:account_list') + "?_export=csv"
        context['view_name'] = _("Accounts")

        return context


class CreateAccount(PermissionRequiredMixin, CreateBreadcrumbMixin, CreateWithInlinesView):
        
    permission_required = 'accounts.add_account'
    
    model = Account
    form_class = AccountForm
    inlines = [AccountUserInlineFormSet, ZoneInlineFormSet, AlarmCodeInlineFormSet]
    
    template_name = 'generic/form.html'
    success_url = reverse_lazy('accounts:account_list')

    def get_context_data(self, **kwargs):
        context = super(CreateAccount, self).get_context_data(**kwargs)

        context['view_name'] = _("Create Account")

        return context


class DetailsAccount(PermissionRequiredMixin, DetailBreadcrumbMixin, UpdateWithInlinesView, DetailView):
        
    permission_required = 'accounts.view_account'
    
    model = Account
    form_class = AccountForm
    inlines = [AccountUserInlineFormSet, ZoneInlineFormSet]

    template_name = 'generic/form.html'
    
    def get_form_kwargs(self):
        # Get the default form kwargs
        kwargs = super().get_form_kwargs()
                
        # Add any additional parameters you want to pass to the form
        kwargs['details'] = True
        
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super(DetailsAccount, self).get_context_data(**kwargs)
        
        context['details'] = True
        context['view_name'] = _("Accounts Details")
        #context['history'] = serializers.serialize("python", self.get_queryset().first().history.all())

        return context
    
    def get_queryset(self):
        # Customize the queryset as needed (e.g., filter by user, etc.)
        return Account.objects.filter(pk=self.kwargs["pk"])


class UpdateeAccount(PermissionRequiredMixin, UpdateBreadcrumbMixin, UpdateWithInlinesView):
    
    permission_required = 'accounts.view_account'
    
    model = Account
    form_class = AccountForm
    inlines = [AccountUserInlineFormSet, ZoneInlineFormSet]
    
    formset_kwargs = {'form_kwargs': {'test': False}}

    template_name = 'generic/form.html'
    success_url = reverse_lazy('accounts:account_list')
    
    def get_context_data(self, **kwargs):
        context = super(UpdateeAccount, self).get_context_data(**kwargs)
        
        context['view_name'] = _("Update Account")

        return context
    
    def get_queryset(self):
        # Customize the queryset as needed (e.g., filter by user, etc.)
        return Account.objects.filter(pk=self.kwargs["pk"])
    
    
class DeleteAccount(PermissionRequiredMixin, DeleteBreadcrumbMixin, DeleteView):
    
    permission_required = 'accounts.delete_account'
    
    model = Account
    template_name = 'generic/confirm-delete.html'

    success_url = reverse_lazy("account_list")
    
    
class ListInstallationCompanies(PermissionRequiredMixin, ListBreadcrumbMixin, ExportMixin, SingleTableMixin, FilterView):
    
    permission_required = 'accounts.view_account'
    
    model = InstallationCompany
    table_class = InstallationCompanyTable 
    paginator_class = LazyPaginator
    
    filterset_class = InstallationCompanyFilter

    template_name = 'generic/list.html'
    
    def get_context_data(self, **kwargs):
        context = super(ListInstallationCompanies, self).get_context_data(**kwargs)
        
        context['add_url'] = reverse_lazy('accounts:installationcompany_create')
        context['export_url'] = reverse_lazy('accounts:installationcompany_list') + "?_export=csv"
        context['view_name'] = _("Installation Companies")

        return context    


class CreateInstallationCompany(PermissionRequiredMixin, CreateBreadcrumbMixin, CreateWithInlinesView):
        
    permission_required = 'accounts.add_account'
    
    model = InstallationCompany
    form_class = InstallationCompanyForm

    template_name = 'generic/form.html'
    success_url = reverse_lazy('accounts:installationcompany_list')

    def get_context_data(self, **kwargs):
        context = super(CreateInstallationCompany, self).get_context_data(**kwargs)
        
        context['view_name'] = _("Create Installation Company")

        return context
    

class UpdateeInstallationCompany(PermissionRequiredMixin, UpdateBreadcrumbMixin, UpdateWithInlinesView):
    
    permission_required = 'accounts.view_account'
    
    model = InstallationCompany
    form_class = InstallationCompanyForm
    
    template_name = 'generic/form.html'
    success_url = reverse_lazy('accounts:installationcompany_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateeInstallationCompany, self).get_context_data(**kwargs)
        
        context['view_name'] = _("Update Installation Company")

        return context
    
    def get_queryset(self):
        # Customize the queryset as needed (e.g., filter by user, etc.)
        return InstallationCompany.objects.filter(pk=self.kwargs["pk"])
    
    
class DetailsInstallationCompany(PermissionRequiredMixin, DetailBreadcrumbMixin, UpdateWithInlinesView, DetailView):
    
    permission_required = 'accounts.view_account'
    
    model = InstallationCompany
    form_class = InstallationCompanyForm
    
    template_name = 'generic/form.html'
    
    def get_form_kwargs(self):
        # Get the default form kwargs
        kwargs = super().get_form_kwargs()
                
        # Add any additional parameters you want to pass to the form
        kwargs['details'] = True
        
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super(DetailsInstallationCompany, self).get_context_data(**kwargs)
        
        context['details'] = True
        context['view_name'] = _("Installation Company Details")

        return context
    
    
    def get_queryset(self):
        # Customize the queryset as needed (e.g., filter by user, etc.)
        return InstallationCompany.objects.filter(pk=self.kwargs["pk"])
    
    
class DeleteInstallationCompany(PermissionRequiredMixin, DeleteBreadcrumbMixin, DeleteView):
    
    permission_required = 'accounts.delete_account'
    
    model = InstallationCompany
    template_name = 'generic/confirm-delete.html'

    success_url = reverse_lazy("installationcompany_list")
    
    
class ListCities(PermissionRequiredMixin, ExportMixin, ListBreadcrumbMixin, SingleTableMixin, FilterView):
    
    permission_required = 'accounts.view_account'
    
    model = City
    table_class = CityTable 
    paginator_class = LazyPaginator
    
    filterset_class = CityFilter

    template_name = 'generic/list.html'

    def get_context_data(self, **kwargs):
        context = super(ListCities, self).get_context_data(**kwargs)
        
        context['add_url'] = reverse_lazy('accounts:city_create')
        context['export_url'] = reverse_lazy('accounts:city_list') + "?_export=csv"
        context['view_name'] = _("Cities")

        return context    


class CreateCity(PermissionRequiredMixin, CreateBreadcrumbMixin, CreateView):
        
    permission_required = 'accounts.add_account'
    
    model = City
    form_class = CityForm

    template_name = 'generic/form.html'
    success_url = reverse_lazy('accounts:city_list')

    def get_context_data(self, **kwargs):
        context = super(CreateCity, self).get_context_data(**kwargs)
        
        context['view_name'] = _("Create City")

        return context


class DetailsCity(PermissionRequiredMixin, DetailBreadcrumbMixin, UpdateView):
    
    permission_required = 'accounts.view_account'
    
    model = City
    form_class = CityForm
    
    template_name = 'generic/form.html'

    def get_form_kwargs(self):
        # Get the default form kwargs
        kwargs = super().get_form_kwargs()
                
        # Add any additional parameters you want to pass to the form
        kwargs['details'] = True
        
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super(DetailsCity, self).get_context_data(**kwargs)
        
        context['details'] = True
        context['view_name'] = _("City Details")

        return context
        
    def get_queryset(self):
        # Customize the queryset as needed (e.g., filter by user, etc.)
        return City.objects.filter(pk=self.kwargs["pk"])
    

class UpdateeCity(PermissionRequiredMixin, UpdateBreadcrumbMixin, UpdateView):
    
    permission_required = 'accounts.view_account'
    
    model = City
    form_class = CityForm
    
    template_name = 'generic/form.html'
    success_url = reverse_lazy('accounts:city_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateeCity, self).get_context_data(**kwargs)
        
        context['view_name'] = _("Update City")

        return context
    
    def get_queryset(self):
        # Customize the queryset as needed (e.g., filter by user, etc.)
        return City.objects.filter(pk=self.kwargs["pk"])
    
    
class DeleteCity(PermissionRequiredMixin, DeleteBreadcrumbMixin, DeleteView):
    
    permission_required = 'accounts.delete_account'
    
    model = City
    template_name = 'generic/confirm-delete.html'

    success_url = reverse_lazy("city_list")
    
    
class ListGroups(PermissionRequiredMixin, ExportMixin, ListBreadcrumbMixin, SingleTableMixin, FilterView):
    
    permission_required = 'accounts.view_account'
    
    model = Group
    table_class = GroupTable 
    paginator_class = LazyPaginator
    
    filterset_class = GroupFilter

    template_name = 'generic/list.html'

    def get_context_data(self, **kwargs):
        context = super(ListGroups, self).get_context_data(**kwargs)
        
        context['add_url'] = reverse_lazy('accounts:group_create')
        context['export_url'] = reverse_lazy('accounts:group_list') + "?_export=csv"
        context['view_name'] = _("Cities")

        return context    


class CreateGroup(PermissionRequiredMixin, CreateBreadcrumbMixin, CreateView):
        
    permission_required = 'accounts.add_account'
    
    model = Group
    form_class = GroupForm

    template_name = 'generic/form.html'
    success_url = reverse_lazy('accounts:group_list')

    def get_context_data(self, **kwargs):
        context = super(CreateGroup, self).get_context_data(**kwargs)
        
        context['view_name'] = _("Create Group")

        return context


class DetailsGroup(PermissionRequiredMixin, DetailBreadcrumbMixin, UpdateView):
    
    permission_required = 'accounts.view_account'
    
    model = Group
    form_class = GroupForm
    
    template_name = 'generic/form.html'

    def get_form_kwargs(self):
        # Get the default form kwargs
        kwargs = super().get_form_kwargs()
                
        # Add any additional parameters you want to pass to the form
        kwargs['details'] = True
        
        return kwargs
    
    def get_context_data(self, **kwargs):
        context = super(DetailsGroup, self).get_context_data(**kwargs)
        
        context['details'] = True
        context['view_name'] = _("Group Details")

        return context
        
    def get_queryset(self):
        # Customize the queryset as needed (e.g., filter by user, etc.)
        return Group.objects.filter(pk=self.kwargs["pk"])
    

class UpdateeGroup(PermissionRequiredMixin, UpdateBreadcrumbMixin, UpdateView):
    
    permission_required = 'accounts.view_account'
    
    model = Group
    form_class = GroupForm
    
    template_name = 'generic/form.html'
    success_url = reverse_lazy('accounts:group_list')

    def get_context_data(self, **kwargs):
        context = super(UpdateeGroup, self).get_context_data(**kwargs)
        
        context['view_name'] = _("Update Group")

        return context
    
    def get_queryset(self):
        # Customize the queryset as needed (e.g., filter by user, etc.)
        return Group.objects.filter(pk=self.kwargs["pk"])
    
    
class DeleteGroup(PermissionRequiredMixin, DeleteBreadcrumbMixin, DeleteView):
    
    permission_required = 'accounts.delete_account'
    
    model = Group
    template_name = 'generic/confirm-delete.html'

    success_url = reverse_lazy("Group_list")