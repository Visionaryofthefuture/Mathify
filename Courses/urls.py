from django.urls import path
from . import views, edit_methods, chart_view

urlpatterns = [
    path('', views.home, name = 'home'),
    path('categories/', views.get_category, name = 'categories'),
    path('search/', views.search_bar, name = "search_results"),
    path('course_description/<int:pk>/', views.course_detail , name = 'course_description'),
    path('course_add/', views.course_addition, name = "course_add"),
    path('course_edit/<int:course_id>/',edit_methods.edit_course, name = 'course_edit'),
    path('course_enroll/<int:course_id>/', views.enroll, name = "course_enroll"),
    path('add_section/<int:course_id>/', edit_methods.section_create, name='add_section'),
    path('course_delete/<int:pk>', edit_methods.delete_course, name = 'course_delete')
]


urlpatterns+=[ path('course/<int:course_id>/section/<int:section_id>/edit/', edit_methods.section_edit, name='section_edit'),
    path('section/<int:section_id>/lesson/add/', edit_methods.lesson_add, name='lesson_add'),
    path('section/<int:section_id>/lesson/<int:lesson_id>/edit/', edit_methods.lesson_edit, name='lesson_edit'),
    path('section/<int:section_id>/lesson/<int:lesson_id>/delete/', edit_methods.lesson_delete, name='lesson_delete'),
    path('course_video/<int:pk>/', views.course_video, name  = "course_video"),
    path('chatbot/', views.chatbot, name = 'chatbot')]

urlpatterns += [    path('enrollment_chart/', chart_view.enrollment_chart, name='enrollment_chart'),
]