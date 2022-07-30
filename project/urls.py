from django.urls import path
from project import views

app_name = "project"

urlpatterns = [
    path('<pk>/delete/', views.ProjectDeleteView.as_view(), name='deleteproject'),
    path('<pk>/update/', views.UpdateProjectView.as_view(), name='updateproject'),
    path('list/',views.ProjectListView.as_view(), name ='projectlist'),
    path('',views.ProjectAddShowView.as_view(), name ='project'),
]
