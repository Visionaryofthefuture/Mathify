
from django.urls import path
from .import views
urlpatterns = [
    path('instructor_register/', views.register_instructor, name ="instructor_register"),
    path('student_register/', views.register_student, name = "student_register"),
    path('user_login/', views.user_login, name = "user_login"),
    path('user_logout/', views.user_logout, name = "user_logout"),
    path('about_us', views.aboutus, name = "about_us"),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
]
