from django.db import models
import datetime
from django.utils import timezone

class Courses(models.Model):
    coursename = models.CharField(max_length=200)
    instructorname = models.CharField(max_length=100)
    startedfrom = models.DateTimeField('Started from')
    def __str__(self):
        return self.coursename

    def recently_published(self):
        return self.startedfrom >= timezone.now() - datetime.timedelta(days = 1)

class Details(models.Model):

    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    coursetype = models.CharField(max_length=500)
    your_choice = models.BooleanField(default=False)
    def __str__(self):
        return str(self.coursetype)

