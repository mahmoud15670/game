from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.views import generic

class UserView(generic.FormView):
    template_name = 'index.html'
    form_class = Myform
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponse('done')
        return render(request, self.template_name ,{'form':form})
    
    def get(self, request):
        form = self.form_class
        return render(request, self.template_name ,{'form':form})