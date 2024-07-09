from django.urls import path
from . import views, edit_methods


urlpatterns = [
    path('', views.home, name = 'home'),
    path('search/', views.search_bar, name = "search_results"),
    path('course_description/<int:pk>/', views.course_detail , name = 'course_description'),
    path('course_add/', views.course_addition, name = "course_add"),
    path('course_edit/<int:course_id>/',edit_methods.edit_course, name = 'course_edit'),
    path('course_enroll/<int:course_id>/', views.enroll, name = "course_enroll")
]

