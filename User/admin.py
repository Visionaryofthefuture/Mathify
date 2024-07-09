from django.contrib import admin
from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from Courses.models import Category, Course, Enrollment
from User.models import User

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'category', 'price', 'level', 'Language')
    search_fields = ('title', 'instructor__email', 'category__name')

class CustomUserAdmin(admin.ModelAdmin):
    model = User

    def delete_model(self, request, obj):
        try:
            with transaction.atomic():
                if hasattr(obj, 'courses'):
                    obj.courses.all().delete()  # Delete all courses related to this user
                obj.delete()  # Delete the user
        except ObjectDoesNotExist:
            obj.delete()
        except Exception as e:
            self.message_user(request, f"Error deleting user: {e}")

    def delete_queryset(self, request, queryset):
        for obj in queryset:
            self.delete_model(request, obj)

class Enrollment_admin(admin.ModelAdmin):
    list_display = ('student', 'course_enrolled_to')
    search_fields = list_display

admin.site.register(User, CustomUserAdmin)
admin.site.register(Category)
admin.site.register(Course, CourseAdmin)
admin.site.register(Enrollment, Enrollment_admin)