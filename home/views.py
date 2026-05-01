from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout
from home.models import Profile  # Import Profile model

def home(request):
    return render(request, 'home/index.html')

def logout_view(request):
    logout(request)
    return redirect("index")
def logged_in(request):
    return render(request,'home/logged_in.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get("signup-username")
        password = request.POST.get("signup-password")
        confirm_password = request.POST.get("signup-confirm-password")
        role = request.POST.get("role")  

        if User.objects.filter(username=username).exists():
            messages.error(request, "User already exists ❌")
        elif confirm_password != password:
            messages.error(request, "Passwords do not match ❌")
        elif role not in ['admin', 'teacher']:
            messages.error(request, "Please select a valid role ❌")
        else:
            user = User(username=username)
            user.set_password(password)
            user.save()
            Profile.objects.create(user=user, role=role)
            messages.success(request, "Signup successful ✅")
            return redirect("login")

    return render(request, 'home/Sign_up.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get("login-username")
        password = request.POST.get("login-password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect("logged_in")
        else:
            messages.error(request, "Invalid credentials ❌, please Sign-Up First")
            return redirect("signup")

    return render(request, 'home/login.html')

def forgot_password(request):
    if request.method == "POST":
        username = request.POST.get("login-username")
        password = request.POST.get("password_tow")
        confirm_password = request.POST.get("confirm_password_tow")

        if confirm_password != password:
            messages.error(request, "Passwords do not match ❌")
        else:
            try:
                user = User.objects.get(username=username)
                user.set_password(password)
                user.save()
                messages.success(request, "Password reset successfully ✅")
                return redirect("login")
            except User.DoesNotExist:
                messages.error(request, "User not found ❌")

    return render(request, 'home/Forgot.html')