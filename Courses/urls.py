from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name = 'home'),
    path('search/', views.search_bar, name = "search_results"),
    path('course_description/<int:pk>/', views.course_detail , name = 'course_description'),
    path('course_add/', views.course_addition, name = "course_add"),
]

