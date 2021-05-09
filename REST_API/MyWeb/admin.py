from django.contrib import admin
from .models import Student, details
# Register your models here.
admin.site.register(Student)
admin.site.register(details)
#class StudentAdmin(admin.ModelAdmin):
 #   list_display = ['id','roll_no','name','city','colleges']