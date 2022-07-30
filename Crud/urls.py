from django.contrib import admin
from django.urls import path, include
from Crud import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/', include('company.urls')),
    path('department/', include('department.urls')),
    path('employee/',include('employee.urls')),
    path('project/',include('project.urls')),
    path('', views.index),
]
