from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Courses import urls as course_urls
from User import urls as User_urls
import django_ckeditor_5.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(course_urls)),
    path('', include(User_urls)),
    path('ckeditor5/', include(django_ckeditor_5.urls)),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)