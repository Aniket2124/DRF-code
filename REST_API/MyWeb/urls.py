from django.urls import path
from .import views


urlpatterns = [

    path('', views.Student, name='Home Page'),



 ]