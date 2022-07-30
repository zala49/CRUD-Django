from django.urls import path
from .views import CompanyDeleteView, CompanyAddShowView, CompanyListView, UpdateCompanyView

app_name = "company"

urlpatterns = [
    path("<pk>/delete", CompanyDeleteView.as_view(), name="deletecompany"),
    path('<pk>/update/', UpdateCompanyView.as_view(), name='updatecompany'),
    path('list/', CompanyListView.as_view(), name ='companylist'),
    path('', CompanyAddShowView.as_view(), name ='company'),
]
