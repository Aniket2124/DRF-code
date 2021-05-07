from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Student(request):
    return HttpResponse('<h1>Admission Home Page</h1>')