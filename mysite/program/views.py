from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class MyView(View):
    result='hi'
    def get(self, request):

        return HttpResponse(self.result)

class greet(MyView):
    result='bye'
