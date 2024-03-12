from django.urls import path

from .views import ListAccounts, CreateAccount, UpdateeAccount, DeleteAccount

urlpatterns = [
    path('accounts/list', ListAccounts.as_view(), name='account_list'),
    path('accounts/create_update/', CreateAccount.as_view(), name='account_create'),
    path('accounts/create_update/<int:pk>', UpdateeAccount.as_view(), name='account_update'),
    path('accounts/view/<int:pk>', DeleteAccount.as_view(), name='account_delete'),

]
