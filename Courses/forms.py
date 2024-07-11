from django import forms
from .models import Course, Lesson, Section

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


class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = ['title', 'order']

    def __init__(self, *args, **kwargs):
        super(SectionForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})


class SectionEditForm(forms.ModelForm):
    section_choice = forms.ModelChoiceField(
        queryset=Section.objects.all(),
        required=False,
        label='Select Section to Edit',
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = Section
        fields = ['section_choice', 'title', 'order']

    def __init__(self, *args, **kwargs):
        super(SectionEditForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'video', 'youtube_url', 'content', 'order']

    def __init__(self, *args, **kwargs):
        super(LessonForm, self).__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})