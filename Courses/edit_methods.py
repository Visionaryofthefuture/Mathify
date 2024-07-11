from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *

def edit_course(request, course_id):
    course = get_object_or_404(Course,pk = course_id)
    sections = Section.objects.filter(course = course)
    if request.method == "POST":
        form = CourseEditForm(request.POST, request.FILES, instance = course)
        if form.is_valid():
            form.save()
            return redirect('course_description', pk=course.pk)
    else:
        form = CourseEditForm(instance=course)
    
    return render(request, 'instructors/course_edit.html', {'form': form, 'course': course, 'item': sections})


def section_create(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            section = form.save(commit=False)
            section.course = course
            if Section.objects.filter(course=course, order=section.order).exists():
                form.add_error('order', 'A section with this order already exists for this course.')
            else:
                section.save()
                return redirect('course_description', pk=course.pk)
    else:
        form = SectionForm()
    
    return render(request, 'Lessons/section_form.html', {'form': form, 'course': course})


def section_edit(request, course_id, section_id):
    course = get_object_or_404(Course, id=course_id)
    section = get_object_or_404(Section, id=section_id, course=course)
    lessons = section.lessons.all()
    
    if request.method == 'POST':
        form = SectionForm(request.POST, instance=section)
        if form.is_valid():
            form.save()
            return redirect('instructor_dashboard')
    else:
        form = SectionForm(instance=section)
    
    return render(request, 'Lessons/section_edit_form.html', {'form': form, 'course': course, 'section': section, 'lessons': lessons})

def lesson_add(request, section_id):
    section = get_object_or_404(Section, id=section_id)
    
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES)
        if form.is_valid():
            lesson = form.save(commit=False)
            lesson.section = section
            lesson.save()
            return redirect('section_edit', course_id=section.course.id, section_id=section.id)
    else:
        form = LessonForm()
    
    return render(request, 'Lessons/lesson_form.html', {'form': form, 'section': section})

def lesson_edit(request, section_id, lesson_id):
    section = get_object_or_404(Section, id=section_id)
    lesson = get_object_or_404(Lesson, id=lesson_id, section=section)
    
    if request.method == 'POST':
        form = LessonForm(request.POST, request.FILES, instance=lesson)
        if form.is_valid():
            form.save()
            return redirect('section_edit', course_id=section.course.id, section_id=section.id)
    else:
        form = LessonForm(instance=lesson)
    
    return render(request, 'Lessons/lesson_form.html', {'form': form, 'section': section})

def lesson_delete(request, section_id, lesson_id):
    section = get_object_or_404(Section, id=section_id)
    lesson = get_object_or_404(Lesson, id=lesson_id, section=section)
    
    if request.method == 'POST':
        lesson.delete()
        return redirect('section_edit', course_id=section.course.id, section_id=section.id)
    
    return render(request, 'Lessons/lesson_confirm_delete.html', {'lesson': lesson, 'section': section})