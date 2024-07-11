
from django.urls import path
from .import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('instructor_register/', views.register_instructor, name ="instructor_register"),
    path('student_register/', views.register_student, name = "student_register"),
    path('user_login/', views.user_login, name = "user_login"),
    path('user_logout/', views.user_logout, name = "user_logout"),
    path('about_us', views.aboutus, name = "about_us"),
    path('student_dashboard/', views.student_dashboard, name='student_dashboard'),
    path('instructor_dashboard/', views.instructor_dashboard, name = "instructor_dashboard"),
]


urlpatterns += [
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
'''

urlpatterns += [
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
     path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='authentication/password_reset_confirm.html'),
         name='password_reset_confirm'),
]

'''

