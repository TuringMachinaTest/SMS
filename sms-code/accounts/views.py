from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from braces.views import PermissionRequiredMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django_filters.views import FilterView
from django_tables2 import LazyPaginator, SingleTableMixin, SingleTableView
from extra_views import CreateWithInlinesView, InlineFormSetFactory, UpdateWithInlinesView

from accounts.filters import AccountFilter

from .tables import AccountsTable

from .forms import AccountForm, AccountUserForm, AccountUserInlineFormSet, CityForm
from .models import Account, AccountUser


class ListAccounts(PermissionRequiredMixin, SingleTableMixin, FilterView):
    
    permission_required = 'accounts.view_account'
    
    model = Account
    table_class = AccountsTable 
    paginator_class = LazyPaginator
    
    filterset_class = AccountFilter

    template_name = 'accounts/list.html'


class CreateAccount(PermissionRequiredMixin, CreateWithInlinesView):
        
    permission_required = 'accounts.add_account'
    
    model = Account
    form_class = AccountForm
    inlines = [AccountUserInlineFormSet]

    template_name = 'accounts/create-update.html'
    success_url = "accounts/list"
    
    def get_form_kwargs(self):
        # Get the default form kwargs
        kwargs = super().get_form_kwargs()
        
        # Add any additional parameters you want to pass to the form
        kwargs['has_permissions'] = self.request.user.has_perm("accounts.add_account")
        
        return kwargs



class UpdateeAccount(PermissionRequiredMixin, UpdateWithInlinesView):
    
    permission_required = 'accounts.view_account'
    
    model = Account
    form_class = AccountForm
    inlines = [AccountUserInlineFormSet]
    
    template_name = 'accounts/create-update.html'
    success_url = "accounts/list"
    
    def get_form_kwargs(self):
        # Get the default form kwargs
        kwargs = super().get_form_kwargs()
        
        # Add any additional parameters you want to pass to the form
        kwargs['has_permissions'] = self.request.user.has_perm("accounts.change_account")
        
        return kwargs
    
    def get_queryset(self):
        # Customize the queryset as needed (e.g., filter by user, etc.)
        return Account.objects.filter(pk=self.kwargs["pk"])
    

class DeleteAccount(PermissionRequiredMixin, DeleteView):
    
    permission_required = 'accounts.delete_account'
    
    model = Account
    template_name = 'shared/confirm-delete.html'

    success_url = reverse_lazy("account_list")