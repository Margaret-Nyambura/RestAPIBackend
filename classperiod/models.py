from django.db import models

# Create your models here.

class ClassPeriod(models.Model):
   start_time=models.TimeField()
   end_time=models.TimeField()
   course=models.CharField(max_length=20)
   classroom=models.CharField(max_length=10)
   day_of_the_week=models.DateField()
   def __str__(self):
        return f"{self.start_time} {self.classroom}"
