from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from.models import Student
# Create your views here.
def Courses(request):
    st=Student.objects.all()
    template=loader.get_template('MyWeb/Courses.html')
    context={
        'st':st,
    }
    return HttpResponse(template.render(context, request))


def details(request, Student_name):
    try:
        name=Student.objects.get(pk=Student_name)
    except Student.DoesNotExist:
        raise Http404("Student details not available")

    return render(request, 'MyWeb/detail.html',{'name':name})