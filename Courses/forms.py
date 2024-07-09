from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['image', 'title', 'text', 'category', 'price', 'level', 'duration', 'Language',]

class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['image', 'title', 'text', 'category', 'price', 'level', 'duration', 'Language',]
    def __init__(self, *args, **kwargs):
            super(CourseEditForm, self).__init__(*args, **kwargs)
            for _, field in self.fields.items():
                if field.widget.__class__.__name__ != 'FileInput':
                    field.widget.attrs.update({'class': 'form-control'})
                else:
                    field.widget.attrs.update({'class': 'form-control-file'})
            
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
