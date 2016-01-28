import datetime
from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.conf import settings
# Create your models here.


class UserProfile(models.Model):
    Name = models.CharField(max_length=100)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True))
    password = models.CharField(max_length=32, widget=forms.PasswordInput)
    mobile_no = models.IntegerField(max_length=13)

    def __unicode__(self):
        return self.email


class Employee(UserProfile):
    institute=models.CharField(max_length=100)
    city=models.CharField(max_length=50)
    address=models.CharField(max_length=250)
    degree=models.CharField(max_length=20)
    stream=models.CharField(max_length=70)
    year =models.DateTimeField()
    graduation_year=models.DateTimeField()
    Performance=models.CharField(max_length=100)
    marks_12=models.CharField(max_length=100)
    marks_10=models.CharField(max_length=100)
    skills=models.TextField()
    job_type=models.TextField()
    job_city=models.TextField()
    Work Experience=models.TextField()


class Employer(UserProfile):
    org_name=models.CharField(max_length=100)
    org_website=models.CharField(max_length=50)
    description=models.models.TextField()


class JobEntry(models.Model):
    start_date=models.DateTimeField()
    package=models.CharField(max_length=100)
    posted_date=models.DateTimeField
    deadline=models.DateTimeField
    no_position=models.IntegerField()
    job_description=models.TextField()
    Filled=1
    Not_Filled = 2
    STATUS_CHOICES = ((Filled, 'Filled'),(Not_Filled, 'Not_Filled'),)
    status = models.IntegerField(choices=STATUS_CHOICES, default=Not_Filled)

    author = models.ForeignKey(Employee)
