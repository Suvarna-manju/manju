from django.db import models

# Create your models here.
class ContactInfo1(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField()
    address =models.CharField(max_length=70)
class StudentInfo1(models.Model):
    rollno =models.IntegerField()
    marks =models.IntegerField()
class TeachearInfo1(ContactInfo1) :
    subject =models.CharField(max_length=60)
    salary =models.FloatField()