from django.shortcuts import render
from tasks.models import Task
from django.shortcuts import redirect
from django.contrib import messages
# include template tags
# Create your views here.

def student_dashboard(request):
    if hasattr(request.user, 'profile') and request.user.profile.role == 'admin':
        tasks = Task.objects.filter(is_completed=False)
        return render(request, 'admin/Admin_dashboard.html', {'tasks': tasks})
    else:
        messages.error(request, "You are not authorized to access the Admin Dashboard!")
        return redirect('index')

def add_task(request):
    if hasattr(request.user, 'profile') and request.user.profile.role == 'admin':
        if request.method == "POST":
            task_id = request.POST.get("task_id")
            title = request.POST.get("title")
            teacher_name = request.POST.get("teacher_name")
            description = request.POST.get("description")
            priority = request.POST.get("priority")

            # ✅ check if a task with the same ID already exists
            if Task.objects.filter(id=task_id).exists():
                messages.error(request, "Task with this ID already exists ❌")
            else:
                Task.objects.create(
                    id=task_id,
                    name=title,
                    teacher_name=teacher_name,
                    description=description,
                    priority=priority
                )
                messages.success(request, "Task added successfully ✅")

            return redirect("add_task")

        return render(request, "admin/insert_new.html")
    else:
        messages.error(request, "You are not authorized to access the Admin Dashboard!")
        return redirect('index')


def view_available_tasks(request):
    if hasattr(request.user, 'profile') and request.user.profile.role == 'admin':
        tasks = Task.objects.filter(is_completed=False)
        return render(request, "admin/View_Available_Tasks.html", {"tasks": tasks})
    else:
        messages.error(request, "You are not authorized to access the Admin Dashboard!")
        return redirect('index')



def edit_task(request):
    if hasattr(request.user, 'profile') and request.user.profile.role == 'admin':
        if request.method == "POST":
            task_id = request.POST.get("task_id")
            try:
                task = Task.objects.get(id=task_id)  
                task.name = request.POST.get("task_title")
                task.teacher_name = request.POST.get("teacher_name")
                task.description = request.POST.get("description")
                task.priority = request.POST.get("priority")
                task.save()
                messages.success(request, "Task updated successfully ✅")
            except Task.DoesNotExist:
                messages.error(request, "Task not found ❌")
            return redirect("edit_task")

        return render(request, "admin/edit_task.html")
    else:
        messages.error(request, "You are not authorized to access the Admin Dashboard!")
        return redirect('index')

def delete_task(request):
    if hasattr(request.user, 'profile') and request.user.profile.role == 'admin':
        if request.method == "POST":
            task_id = request.POST.get("task_id")
            try:
                task = Task.objects.get(id=task_id)
                task.delete()
                messages.success(request, "Task deleted successfully ✅")
            except Task.DoesNotExist:
                messages.error(request, "Task with this ID does not exist ❌")
            return redirect("delete_task")  # Redirect to the delete task page 
            

        return render(request, "admin/delete_task.html")
    else:
        messages.error(request, "You are not authorized to access the Admin Dashboard!")
        return redirect('index')
