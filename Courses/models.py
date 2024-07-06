from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from User.models import User
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
