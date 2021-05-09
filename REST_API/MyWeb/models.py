from django.db import models
import datetime

# Create your models here.
class Student(models.Model):
    roll_no = models.IntegerField()
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    college = models.CharField(max_length=100)


    def __str__(self):
        return self.name

class details(models.Model):
    Stud_Name=models.ForeignKey(Student, on_delete=models.CASCADE)
    Faculty=models.CharField(max_length=500)
    #Year=models.IntegerField('Year')
    YEAR_CHOICES = [(r, r) for r in range(1984, datetime.date.today().year + 1)]
    year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)

    def __str__(self):
        return self.Faculty