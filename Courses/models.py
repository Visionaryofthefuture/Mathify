from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from User.models import User
from datetime import timedelta
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Course(models.Model):
    image = models.ImageField(upload_to="images/", default="default.png")
    title = models.CharField(max_length= 25, blank = False)
    Instructor = models.ForeignKey(User, related_name= "User",on_delete= models.CASCADE)
    text=CKEditor5Field('Text', config_name='extends', default = "text" )
    category = models.ForeignKey(Category,related_name="category", on_delete= models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, default= 0)
    timestamp = models.DateTimeField(auto_now=True)
    level = models.CharField(max_length=20, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], default="Beginner")
    duration = models.DurationField(default = timedelta)  # Course duration
    Language = models.CharField(default= "English", max_length= 20)
    def __str__(self):
        return f"{self.Instructor} : {self.title}"

class Applied(models.Model):
    applicant = models.ForeignKey(User, on_delete= models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return f" {self.applicant.first_name} {self.applicant.last_name} : {self.course.title} "
    
class Instructor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="instructor_profile")
    bio = CKEditor5Field('Text', config_name='extends', default = "text" )
    profile_picture = models.ImageField(upload_to="instructors/", default="default.png")
    facebook = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)    
    instagram = models.URLField(max_length= 200, blank  =True, null = True)
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review by {self.user} for {self.course}"

class Section(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="sections")
    title = models.CharField(max_length=100)
    order = models.PositiveIntegerField()  # To maintain the order of sections
    
    def __str__(self):
        return f"{self.course} - {self.title}"
    
class Lecture(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="lectures")
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')  # Video file field
    duration = models.DurationField(default= timedelta)  # Duration of the lecture
    order = models.PositiveIntegerField()  # To maintain the order of lectures
    
    def __str__(self):
        return f"{self.section.course} - {self.section} - {self.title}"
