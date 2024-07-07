from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .models import User
from django.contrib.auth.decorators import login_required
from .forms import InstructorRegistrationForm, StudentRegistrationForm, UserLoginForm, UserProfileForm

def register_instructor(request):
    if request.method == 'POST':
        form = InstructorRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Update this to your instructor dashboard URL
    else:
        form = InstructorRegistrationForm()
    return render(request, 'authentication/register_instructor.html', {'form': form})

def register_student(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = StudentRegistrationForm()
    return render(request, 'authentication/register_student.html', {'form' : form})

def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'authentication/login.html', context)

def user_logout(request):
    logout(request)
    return redirect('home')

def aboutus(request):
    return render(request, 'coursepage/about.html')


@login_required
def student_dashboard(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            data = form.cleaned_data

            # Debugging: Print cleaned data
            print("Cleaned Data:", data)

            # Ensure fields are updated only if provided
            if not data['profile_picture']:
                user.profile_picture = request.user.profile_picture  # retain existing picture if not updated
           
            
            user.save()

            # Debugging: Print updated user data
            print("Updated User:", user)
            
            return redirect('home')
        else:
            # Debugging: Print form errors
            print("Form Errors:", form.errors)
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'coursepage/student_dashboard.html', {'form': form})