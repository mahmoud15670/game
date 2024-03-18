from django.forms import ModelForm
from .models import *

class Myform(ModelForm):
    model = user
    fields = ['name', 'email', 'age', 'single']