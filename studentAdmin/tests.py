from django.urls import path
from . import views
urlpatterns = [
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add_task/', views.add_task, name='add_task'),
    path('view_tasks/', views.view_available_tasks, name='view_tasks'),
    path('edit_task/<str:task_id>/', views.edit_task, name='edit_task'),
]