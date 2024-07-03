from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from .forms import InstructorRegistrationForm, StudentRegistrationForm, UserLoginForm

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