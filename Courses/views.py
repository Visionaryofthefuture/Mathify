from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db.models import Q
from Courses.forms import CourseForm
from django.http import HttpResponse

def home(request):
    user = request.user if request.user.is_authenticated else None
    courses = Course.objects.all().order_by('timestamp')
    params = {'courses': courses, 'user': user}
    return render(request, "coursepage/carrousel.html", params)

def course_detail(request, pk):
    course = get_object_or_404(Course, pk =pk)
    seconds = course.duration.total_seconds()
    hours = int(seconds //3600)
    minutes=  int(seconds % 60) % 60
    seconds = seconds % 60
    try:
        Enrollment_status = Enrollment.objects.get(student = request.user, course_enrolled_to = course)
        enrolled = True
    except Enrollment.DoesNotExist:
        enrolled= False
    context = {'course': course, 'hour': hours, 'minutes': minutes, 'seconds':seconds, 'enrolled': enrolled}
    return render(request, 'coursepage/course_description.html', context)

def search_bar(request):
    result = request.GET.get('q')
    courses = Course.objects.filter(
        Q(title__icontains=result) |
        Q(category__name__icontains=result) |
        Q(text__icontains=result)
    )
    context = {
        'query': result,
        'courses': courses
    }
    return render(request, 'coursepage/search_results.html', context)


def course_addition(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                course = Course.objects.create(
                    image=form.cleaned_data['image'],
                    title=form.cleaned_data['title'],
                    text=form.cleaned_data['text'],
                    category=form.cleaned_data['category'],
                    price=form.cleaned_data['price'],
                    level=form.cleaned_data['level'],
                    duration=form.cleaned_data['duration'],
                    Language=form.cleaned_data['Language'],
                    instructor = request.user
                )
                
                return redirect('course_description', pk=course.pk)  
            
            except Exception as e:
                print(f"Error occurred: {e}")
                
        else:
            print(f"Form errors: {form.errors}")
    
    else:
        form = CourseForm()
    
    context = {
        'form': form,
    }
    return render(request, 'instructors/course_add.html', context)

def enroll(request, course_id):
    course = get_object_or_404(Course, pk = course_id)
    student = request.user # student can be another instructor or a regular student too
    try:
        Enrollment.objects.create(course_enrolled_to = course , student = student)
        return redirect('home')

    except Exception as e:
        print(f"error occured :{e}")
    return HttpResponse("Could not enroll")

