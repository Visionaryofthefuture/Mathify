from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from Courses.models import Enrollment
from .models import User
from Courses.models import Course, Enrollment
from django.contrib.auth.decorators import login_required
from .forms import InstructorRegistrationForm, StudentRegistrationForm, UserLoginForm, UserProfileForm, InstructorProfileForm

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
    num_users = User.objects.all().count
    num_enrollments = Enrollment.objects.all().count
    num_courses = Course.objects.all().count
    num_languages = Course.objects.values('Language').distinct().count()
    num_instructors = User.objects.filter(role = "Instructor").count
    context = {'courses' : num_courses, 'users':num_users, 'instructors': num_instructors, 'languages': num_languages, 'enrollments': num_enrollments}
    return render(request, 'coursepage/about.html', context)


@login_required
def student_dashboard(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            data = form.cleaned_data
            if not data['profile_picture']:
                user.profile_picture = request.user.profile_picture
            user.save()
            return redirect('home')
        else:
            print("Form Errors:", form.errors)
    else:
        form = UserProfileForm(instance=request.user)

    enrolled_courses = Enrollment.objects.filter(student=request.user).select_related('course_enrolled_to')
    
    context = {
        'form': form,
        'enrolled_courses': [enrollment.course_enrolled_to for enrollment in enrolled_courses]
    }
    return render(request, 'coursepage/student_dashboard.html', context)


@login_required
def instructor_dashboard(request):
    if request.method == 'POST':
        form = InstructorProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the same page after saving
        
        else:
            print("Form errors : "  , form.errors)
    else:
        form = InstructorProfileForm(instance=request.user)
    
    instructor_courses = Course.objects.filter(instructor = request.user)
    context = {
        'form': form,
        'instructor_courses': instructor_courses,
    }
    return render(request, 'instructors/instructor_dashboard.html', context)

