from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from User.models import User
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from datetime import timedelta

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Course(models.Model):
    image = models.ImageField(upload_to="images/", default="default.png")
    title = models.CharField(max_length=25, blank=False)
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="courses")
    text = CKEditor5Field('Text', config_name='extends', default="text")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="courses", null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    timestamp = models.DateTimeField(auto_now=True)
    level = models.CharField(max_length=20, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default="Beginner")
    duration = models.DurationField(default=timedelta)
    Language = models.CharField(default="English", max_length=20)

    def __str__(self):
        return f"{self.instructor.first_name} : {self.title}"

class Enrollment(models.Model):
    course_enrolled_to = models.ForeignKey(Course, on_delete= models.CASCADE, related_name = "enrolled_course")
    student = models.ForeignKey(User, on_delete= models.CASCADE, related_name= "enrolled_student")
    enrolled_on = models.DateTimeField(auto_now= True)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} : {self.course_enrolled_to.title} "
    

class Section(models.Model):
    course = models.ForeignKey(Course, on_delete= models.CASCADE, related_name= "course")
    title = models.CharField(max_length= 200)
    order = models.PositiveIntegerField(default= 0)
    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.course} : {self.title} "


class Lesson(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="lessons")
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to="videos/", blank=True, null=True)
    youtube_url = models.URLField(blank =True, null=True)
    content = models.TextField(blank =True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.section} : {self.title}"
