from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    single = models.BooleanField(default=True)