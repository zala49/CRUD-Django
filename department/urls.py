"""Crud URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from department import views

app_name = "department"
urlpatterns = [
    path('<pk>/delete/', views.DepartmentDeleteView.as_view(), name='deletedepartment'),
    path('<pk>/update/', views.UpdateDepartmentView.as_view(), name='updatedepartment'),
    path('list/',views.DepartmentListView.as_view(), name ='departmentlist'),
    path('',views.DepartmentAddShowView.as_view(), name ='department'),
]
