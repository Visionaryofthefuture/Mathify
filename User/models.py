from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from .account import CustomUserManager


roles = (
    ('student', "Student"),
    ('Instructor', "Instructor"),
)

Gender = (
    ('M', "Male"),
    ('F', "Female"),
)

class User(AbstractUser):
    role = models.CharField(choices=roles, max_length=14)
    gender = models.CharField(choices=Gender, max_length=7)
    email = models.EmailField(unique=True, blank=False, error_messages={'unique': "A user with that email already exists."})
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    profile_picture = models.ImageField(upload_to="instructors/", default="default.png")
    facebook = models.URLField(max_length=200, blank=True, null=True)
    twitter = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)    
    instagram = models.URLField(max_length=200, blank=True, null=True)
    bio = models.TextField(null = True, blank = True)
    def __str__(self):
        return f"{self.email}"
    
    def get_full_name(self):
        return self.first_name + ' ' + self.last_name
        
    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Add a unique related_name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    objects = CustomUserManager()
