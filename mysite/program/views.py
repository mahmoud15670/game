from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .forms import *
from django.views import generic

class UserView(generic.FormView):
    template_name = 'index.html'
    form_class = Myform
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('user'))
        return render(request, self.template_name ,{'form':form})
    
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name ,{'form':form})

class UpdateUserView(generic.edit.UpdateView):
    model = user
    fields = '__all__'
    template_name_suffix = '_update_form'
    success_url = '/'