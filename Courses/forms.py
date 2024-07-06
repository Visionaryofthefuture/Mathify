from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['image', 'title', 'text', 'category', 'price', 'level', 'duration', 'Language',]

'''
class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['title', 'order']

class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = ['title', 'video', 'duration', 'order']
        '''
