from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Task
from django.utils import timezone
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

def teacher_dashboard(request):
    if hasattr(request.user, 'profile') and request.user.profile.role == 'teacher':
        return render(request, 'teacher/teacher_dashboard.html')
    else:
        messages.error(request, "You are not authorized to access the Teacher Dashboard!")
        return redirect('index')

def view_available_tasks(request):
    if hasattr(request.user, 'profile') and request.user.profile.role == 'teacher':
        tasks = Task.objects.filter(is_completed=False)
        return render(request, 'teacher/view_available_tasks.html', {'tasks': tasks})
    else:
        messages.error(request, "You are not authorized to access the Teacher Dashboard!")
        return redirect('index')

def view_completed_tasks(request):
    if hasattr(request.user, 'profile') and request.user.profile.role == 'teacher':
        tasks = Task.objects.filter(is_completed=True)
        return render(request, 'teacher/view_completed_tasks.html', {'tasks': tasks})
    else:
        messages.error(request, "You are not authorized to access the Teacher Dashboard!")
        return redirect('index')

def view_details(request):
    if hasattr(request.user, 'profile') and request.user.profile.role == 'teacher':
        tasks = Task.objects.filter(is_completed=False)
        return render(request, 'teacher/view_details.html', {'tasks': tasks})
    else:
        messages.error(request, "You are not authorized to access the Teacher Dashboard!")
        return redirect('index')


def mark_task_completed(request):
    if hasattr(request.user, 'profile') and request.user.profile.role == 'teacher':
        tasks = Task.objects.filter(is_completed=False)
        return render(request, 'teacher/mark_task_completed.html', {'tasks': tasks})
    else:
        messages.error(request, "You are not authorized to access the Teacher Dashboard!")
        return redirect('index')

def search_tasks(request):
    if hasattr(request.user, 'profile') and request.user.profile.role == 'teacher':
        return render(request, 'teacher/search_tasks.html')
    else:
        messages.error(request, "You are not authorized to access the Teacher Dashboard!")
        return redirect('index')
    

def api_mark_task_completed(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            task_name = data.get('task_name')

            task = Task.objects.get(name=task_name)
            task.is_completed = True
            task.completed_date = timezone.now().date()
            task.save()

            return JsonResponse({'success': True, 'message': f'Task \"{task_name}\" marked as completed.'})
        except Task.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Task not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    return JsonResponse({'success': False, 'message': 'Invalid request method.'}, status=405)

def api_search_tasks(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        priority = data.get('priority').lower()
        tasks = Task.objects.filter(priority=priority, is_completed=False)
        tasks_data = [
            {'id': task.id, 'name': task.name, 'priority': task.priority}
            for task in tasks
        ]
        return JsonResponse({'success': True, 'tasks': tasks_data})
    return JsonResponse({'success': False, 'message': 'Invalid request!'}, status=400)