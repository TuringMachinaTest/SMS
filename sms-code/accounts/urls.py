from django.urls import path

from .views import CreatCity, CreatInstallationCompany, DeleteCity, DeleteInstallationCompany, DetailsAccount, DetailsInstallationCompany, ListAccounts, CreateAccount, ListCities, ListInstallationCompanies, UpdateeAccount, DeleteAccount, UpdateeCity, UpdateeInstallationCompany

urlpatterns = [
    path('accounts/list', ListAccounts.as_view(), name='account_list'),
    path('accounts/details/<int:pk>', DetailsAccount.as_view(), name='account_details'),
    path('accounts/create/', CreateAccount.as_view(), name='account_create'),
    path('accounts/update/<int:pk>', UpdateeAccount.as_view(), name='account_update'),
    path('accounts/view/<int:pk>', DeleteAccount.as_view(), name='account_delete'),

    path('installation_company/list', ListInstallationCompanies.as_view(), name='installation_company_list'),
    path('installation_company/details/<int:pk>', DetailsInstallationCompany.as_view(), name='installation_company_details'),
    path('installation_company/create/', CreatInstallationCompany.as_view(), name='installation_company_create'),
    path('installation_company/update/<int:pk>', UpdateeInstallationCompany.as_view(), name='installation_company_update'),
    path('installation_company/view/<int:pk>', DeleteInstallationCompany.as_view(), name='installation_company_delete'),
    
    path('cities/list', ListCities.as_view(), name='city_list'),
    path('cities/details/<int:pk>', ListCities.as_view(), name='city_details'),
    path('cities/create/', CreatCity.as_view(), name='city_create'),
    path('cities/update/<int:pk>', UpdateeCity.as_view(), name='city_update'),
    path('cities/view/<int:pk>', DeleteCity.as_view(), name='city_delete'),
]
