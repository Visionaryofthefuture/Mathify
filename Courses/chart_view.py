import io
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from django.http import HttpResponse
from .models import Course, Enrollment
from django.contrib.auth.decorators import login_required

@login_required
def enrollment_chart(request):
    user = request.user
    courses = Course.objects.filter(instructor=user)
    enrollments = Enrollment.objects.filter(course_enrolled_to__in=courses).values('course_enrolled_to__title', 'enrolled_on')
    
    course_enrollments = {}
    
    for enrollment in enrollments:
        course = enrollment['course_enrolled_to__title']
        date = enrollment['enrolled_on'].date()
        
        if course not in course_enrollments:
            course_enrollments[course] = {}
        
        if date not in course_enrollments[course]:
            course_enrollments[course][date] = 0
        
        course_enrollments[course][date] += 1
    
    # Generate the graph
    plt.figure(figsize=(10, 6))
    
    for course, dates in course_enrollments.items():
        sorted_dates = sorted(dates.items())
        x, y = zip(*sorted_dates)
        plt.plot(x, y, label=course)
    
    plt.xlabel('Date')
    plt.ylabel('Enrollments')
    plt.title('Course Enrollments Over Time')
    plt.legend()
    
    # Save the graph to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    
    # Serve the graph as an image
    return HttpResponse(buf, content_type='image/png')
