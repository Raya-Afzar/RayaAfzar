# company/urls.py

from django.urls import include, path
from django.contrib.auth import views as auth_views

from mysite.project.views import (ProjectCreateView, ProjectListView,
                ProjectDetailView, ProjectDeleteView,)

app_name ='project'
urlpatterns = [
    path('create-project/',ProjectCreateView.as_view(), name='create'),
    path('project-list/',ProjectListView.as_view(), name='list'),
    path('project-detail/<int:pk>/',ProjectDetailView.as_view(), name='detail'),
    path('project-delete/<int:pk>/',ProjectDeleteView.as_view(), name='delete'),

]
