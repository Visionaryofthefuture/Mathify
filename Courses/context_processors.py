from .models import Course
from User.models import Searches
from .views import get_recommended_courses

def recommended_courses(request):
    if request.user.is_authenticated:
        recommended_courses = get_recommended_courses(request.user)
    else:
        recommended_courses = Course.objects.none()
    return {'recommended_courses': recommended_courses}