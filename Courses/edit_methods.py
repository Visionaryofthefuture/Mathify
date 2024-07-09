from django.shortcuts import render, redirect, get_object_or_404
from .forms import CourseEditForm
from .models import Course

def edit_course(request, course_id):
    course = get_object_or_404(Course,pk = course_id)
    if request.method == "POST":
        form = CourseEditForm(request.POST, request.FILES, instance = course)
        if form.is_valid():
            form.save()
            return redirect('course_description', pk=course.pk)  
    else:
        form = CourseEditForm(instance=course)
    return render(request, 'instructors/course_edit.html', {'form': form, 'course': course})
