from django.shortcuts import render
from django.http import HttpResponse
from .forms import *
from django.views import generic

class UserView(generic.FormView):
    def post(self, request):
        form =Myform(request.POST)
        if form.is_valid():
            return HttpResponse('done')
    
    def get(self, request):
        form = Myform
        return render(request, 'index.html' ,{
            'form':form
        })