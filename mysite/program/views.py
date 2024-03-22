from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import *
from django.views import generic

class IndexView(generic.ListView):
    model = user
    template_name = 'index.html'
    context_object_name = 'users'
class UserView(generic.CreateView):
    template_name = 'create_user.html'
    model = user
    fields = '__all__'
    success_url = reverse_lazy('index')

class UserDetailView(generic.DetailView):
    model = user
    template_name = 'user_detail.html'
    context_object_name = 'user'
class UpdateUserView(generic.UpdateView):
    model = user
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('index')

class UserDeleteView(generic.DeleteView):
    model = user
    template_name_suffix = '_confirm_delete'
    success_url = reverse_lazy('index')
