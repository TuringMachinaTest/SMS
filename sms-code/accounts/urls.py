from django.urls import path

from .views import CreatCity, CreatInstallationCompany, DeleteCity, DeleteInstallationCompany, DetailsAccount, DetailsCity, DetailsInstallationCompany, ListAccounts, CreateAccount, ListCities, ListInstallationCompanies, UpdateeAccount, DeleteAccount, UpdateeCity, UpdateeInstallationCompany

urlpatterns = [
    path('accounts/list', ListAccounts.as_view(), name='account_list'),
    path('accounts/details/<int:pk>', DetailsAccount.as_view(), name='account_detail'),
    path('accounts/create/', CreateAccount.as_view(), name='account_create'),
    path('accounts/update/<int:pk>', UpdateeAccount.as_view(), name='account_update'),
    path('accounts/view/<int:pk>', DeleteAccount.as_view(), name='account_delete'),

    path('installation_company/list', ListInstallationCompanies.as_view(), name='installationcompany_list'),
    path('installation_company/details/<int:pk>', DetailsInstallationCompany.as_view(), name='installationcompany_detail'),
    path('installation_company/create/', CreatInstallationCompany.as_view(), name='installation_companycreate'),
    path('installation_company/update/<int:pk>', UpdateeInstallationCompany.as_view(), name='installationcompany_update'),
    path('installation_company/view/<int:pk>', DeleteInstallationCompany.as_view(), name='installationcompany_delete'),
    
    path('cities/list', ListCities.as_view(), name='city_list'),
    path('cities/details/<int:pk>', DetailsCity.as_view(), name='city_detail'),
    path('cities/create/', CreatCity.as_view(), name='city_create'),
    path('cities/update/<int:pk>', UpdateeCity.as_view(), name='city_update'),
    path('cities/view/<int:pk>', DeleteCity.as_view(), name='city_delete'),
]
