from django.db import models

# Create your models here.
from django.utils.datetime_safe import date


class Request(models.Model):
    request_date = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(default=date.today)
    gender = models.CharField(max_length=10)
    nationality = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    pincode = models.IntegerField()
    qualification = models.CharField(max_length=20)
    salary = models.IntegerField()
    pan_number = models.CharField(max_length=20)

    objects = models.Manager()



class Response(models.Model):
    request_id = models.IntegerField()
    response = models.CharField(max_length=20)
    reason = models.CharField(max_length=500)

    objects = models.Manager()
