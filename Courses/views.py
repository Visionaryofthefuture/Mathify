from django.shortcuts import render, get_object_or_404
from .models import Course
from django.db.models import Q
from django.views.decorators.cache import cache_page

def is_instructor(request):
    return request.user.role == "Instructor"

@cache_page(60*15)
def home(request):
    user = request.user if request.user.is_authenticated else None
    courses = Course.objects.all().order_by('timestamp')
    params = {'courses': courses, 'user' : user}
    return render(request, "coursepage/base.html", params)

def course_detail(request, pk):
    course = get_object_or_404(Course, pk = pk)
    context = {'course' : course}
    return render(request, 'coursepage/course_description.html', context)

def search_bar(request):
    result = request.GET.get('q')
    courses = Course.objects.filter(
        Q(title__icontains= result) |
        Q(category__name__icontains= result) |
        Q(text__icontains= result )
    )
    context = {
        'query': result,
        'courses' : courses
    }
    return render(request, 'coursepage/search_results.html', context)