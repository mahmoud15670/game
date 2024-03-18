from django.forms import ModelForm
from .models import *

class Myform(ModelForm):
    class Meta:
        model = user
        fields = ['name', 'email', 'age', 'single']