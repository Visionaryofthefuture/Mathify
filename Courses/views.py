from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db.models import Q
from Courses.forms import CourseForm #,LectureForm, SectionForm



def home(request):
    user = request.user if request.user.is_authenticated else None
    courses = Course.objects.all().order_by('timestamp')
    params = {'courses': courses, 'user': user}
    return render(request, "coursepage/carrousel.html", params)

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    context = {'course': course}
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
                # Create a new Course object from the form data
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
                
                return redirect('course_description', pk=course.pk)  # Redirect to course detail view
            
            except Exception as e:
                print(f"Error occurred: {e}")
                # Handle the exception as needed, e.g., logging, informing the user
                
        else:
            print(f"Form errors: {form.errors}")
    
    else:
        form = CourseForm()
    
    context = {
        'form': form,
    }
    return render(request, 'instructors/course_add.html', context)