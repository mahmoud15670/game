from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from .models import *


class IndexView(generic.ListView):
    queryset = {}
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
    def form_valid(self, form):
        object = form.save()
        for test in object.tests.all():
            result = Result(
                patient=Patient.objects.get(pk=object.id),
                test=test,
                ref=''
            )
            result.save()
            if object.gender == 'male':
                result.ref = test.male_ref
            else:
                result.ref = test.female_ref
            result.save()
        return HttpResponseRedirect(reverse('index'))
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


class TestCreateView(generic.CreateView):
    model = Test
    template_name_suffix = '_create_form'
    fields = '__all__'
    success_url = reverse_lazy('index')

class TestDetilView(PatientDetilView):
    model = Test
    context_object_name = 'test'


class TestEditView(PatientEditView):
    model = Test


class TestDeleteView(PatientDeleteView):
    model = Test
