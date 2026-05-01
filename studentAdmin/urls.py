from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.student_dashboard, name='dashboard'),
    path('view_tasks/', views.view_available_tasks, name='view_tasks'),
    path('add_task/', views.add_task, name='add_task'),
    path('edit_task/', views.edit_task, name='edit_task'),
    path('delete_task/', views.delete_task, name='delete_task'),
]
