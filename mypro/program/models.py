from django.utils import timezone
from django.db import models

# Create your models here.

class Result(models.Model):
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)
    test = models.ForeignKey('Test', on_delete=models.CASCADE)
    result = models.CharField(max_length=20, blank=True)
    ref = models.TextField()

class Patient(models.Model):
    name = models.CharField(max_length=40)
    age = models.PositiveSmallIntegerField()
    date = models.CharField(max_length=5, choices=[
        ('year', 'year'),
        ('month', 'month'),
        ('day', 'day')
    ])
    gender = models.CharField(max_length=6, choices=[
        ('male', 'male'),
        ('female', 'female')
    ])
    dr = models.CharField(max_length=40, blank=True)
    phone = models.CharField(max_length=11, blank=True)
    tests = models.ManyToManyField('Test')
    entry = models.DateTimeField(default=timezone.now(), editable=False)

    def total_price(self):
        price = []
        for test in self.tests.all():
            price.append(test.price)
        return sum(price)

    def add_result(self):
        for test in self.tests.all():
            if test not in [test.test for test in self.result_set.all()]:
                result = Result(
                    patient = Patient.objects.get(pk=self.id),
                    test = test,
                    ref = ''
                )
                if self.gender == 'male':
                    result.ref = test.male_ref
                else:
                    result.ref = test.female_ref
                result.save()

    def __str__(self):
        return self.name


class Test(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField()
    unit = models.CharField(max_length=20, blank=True)
    male_ref = models.TextField(blank=True)
    female_ref = models.TextField(blank=True)

    def __str__(self):
        return self.name



