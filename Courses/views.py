from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from User.models import *
from django.db.models import Q
from Courses.forms import CourseForm
from django.http import HttpResponse
from django.core.cache import cache

def home(request):
    user = request.user if request.user.is_authenticated else None
    courses = Course.objects.all().order_by('timestamp')
    params = {'courses': courses, 'user': user}
    return render(request, "coursepage/carrousel.html", params)


def get_category(request):
    categories = Category.objects.all()
    context = {'category': categories}
    return render(request, 'instructors/categories.html', context)


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    seconds = course.duration.total_seconds()
    hours = int(seconds // 3600)
    minutes = int(seconds % 3600 // 60)
    seconds = int(seconds % 60)
    
    enrolled = False
    if request.user.is_authenticated:
        try:
            Enrollment_status = Enrollment.objects.get(student=request.user, course_enrolled_to=course)
            enrolled = True
        except Enrollment.DoesNotExist:
            enrolled = False
    
    context = {
        'course': course,
        'hour': hours,
        'minutes': minutes,
        'seconds': seconds,
        'enrolled': enrolled,
    }
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
        return redirect('student_dashboard')

    except Exception as e:
        print(f"error occured :{e}")
    return HttpResponse("Could not enroll , Please Check if you are LOGGED IN first.")


def course_video(request, pk):
    course = get_object_or_404(Course, pk = pk)
    sections = Section.objects.filter(course = course).prefetch_related('lessons')
        
    context = {
        'course': course,
        'sections': sections,
       
    }
    return render(request, 'coursepage/course_video.html', context)




CACHE_TIMEOUT = 60 * 60  # 1 hour

def get_recommended_courses(user):
    cache_key = f'recommended_courses_{user.pk}'
    recommended_courses = cache.get(cache_key)
    
    if not recommended_courses:
        user_searches = Searches.objects.filter(searcher=user).values_list('search_term', flat=True)
        recommended_courses_set = set()

        for term in user_searches:
            similar_courses = Course.objects.filter(
                Q(title__icontains=term) |
                Q(category__name__icontains=term) |
                Q(text__icontains=term)
            ).distinct()
            recommended_courses_set.update(similar_courses)

        recommended_courses = list(recommended_courses_set)
        cache.set(cache_key, recommended_courses, CACHE_TIMEOUT)
    
    return recommended_courses


def chatbot(request):
    return render(request, 'chatbot/chatbot.html')