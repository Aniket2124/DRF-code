from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    college = models.CharField(max_length=100)


    def __str__(self):
        return self.name