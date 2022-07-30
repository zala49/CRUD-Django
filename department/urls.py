from django.urls import path
from department import views

app_name = "department"
urlpatterns = [
    path('<pk>/delete/', views.DepartmentDeleteView.as_view(), name='deletedepartment'),
    path('<pk>/update/', views.UpdateDepartmentView.as_view(), name='updatedepartment'),
    path('list/',views.DepartmentListView.as_view(), name ='departmentlist'),
    path('',views.DepartmentAddShowView.as_view(), name ='department'),
]
