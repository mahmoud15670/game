from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import *


class IndexView(generic.ListView):
    queryset = {
        'patients': Patient.objects.all(),
        'tests': Test.objects.all()
    }
    template_name = 'program/index.html'
    context_object_name = 'queries'


class PatientCreateView(generic.CreateView):
    model = Patient
    template_name_suffix = '_create_form'
    fields = '__all__'
    success_url = reverse_lazy('index')


class PatientDetilView(generic.DetailView):
    model = Patient
    template_name_suffix = '_detil'
    context_object_name = 'patient'


class PatientEditView(generic.UpdateView):
    model = Patient
    template_name_suffix = '_update_form'
    fields = '__all__'
    success_url = reverse_lazy('index')


class PatientDeleteView(generic.DeleteView):
    model = Patient
    template_name_suffix = '_delete_form'
    success_url = reverse_lazy('index')


class TestCreateView(PatientCreateView):
    model = Test


class TestDetilView(PatientDetilView):
    model = Test
    context_object_name = 'test'


class TestEditView(PatientEditView):
    model = Test


class TestDeleteView(PatientDeleteView):
    model = Test
