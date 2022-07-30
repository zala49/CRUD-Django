from django.contrib import admin
from django.urls import path
from employee import views

app_name = "employee"
urlpatterns = [
    path('<pk>/delete/', views.EmployeeDeleteView.as_view(), name='deleteemployee'),
    path('<pk>/update/', views.UpdateEmployeeView.as_view(), name='updateemployee'),
    path('list/',views.EmployeeListView.as_view(), name ='employeelist'),
    path('',views.EmployeeAddShowView.as_view(), name ='employee'),
]
