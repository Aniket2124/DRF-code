from django.urls import path
from .import views

urlpatterns = [
    path('', views.Courses,name='Home_Page'),
    path('<int:Student_name>/', views.details,name='Details_Page'),

]