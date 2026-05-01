from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_dashboard, name='teacher_dashboard'),
    path('view_available_tasks/', views.view_available_tasks, name='view_available_tasks'),
    path('view_completed_tasks/', views.view_completed_tasks, name='view_completed_tasks'),
    path('view_details/', views.view_details, name='view_details'),
    path('mark_task_completed/', views.mark_task_completed, name='mark_task_completed'),
    path('search_tasks/', views.search_tasks, name='search_tasks'),
    path('api/mark_task_completed/', views.api_mark_task_completed, name='api_mark_task_completed'),
    path('api/search_tasks/', views.api_search_tasks, name='api_search_tasks'),
]