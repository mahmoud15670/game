from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=40)
    age = models.PositiveSmallIntegerField()
    date = models.CharField(max_length=5, choices=[
        ('year','year')
        ('month','month')
        ('day','day')
    ])
    gender = models.CharField(max_length=6, choices=[
        ('male','male'),
        ('female','female')
    ])
    dr = models.CharField(max_length=40)
    phone = models.CharField(max_length=11)
    