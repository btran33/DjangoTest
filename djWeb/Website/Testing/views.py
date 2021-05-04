from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Courses
from django.template import loader

# Home Page
def Home(request):
    course = Courses.objects.all()
    template = loader.get_template('Testing/Courses.html')
    context ={
        'course':course,
    }
    return HttpResponse(template.render(context, request))

# Details Page
def Details(request, course_id):
    try:
        c = Courses.objects.get(id = course_id)
    except Courses.DoesNotExist:
        raise Http404('Course Not Available')
    return render(request, 'Testing/detail.html', {'course': c})