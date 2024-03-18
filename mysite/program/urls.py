from django.urls import path
from . import views
from django.views import generic

urlpatterns = [
    path('', generic.TemplateView.as_view(template_name='index.html'))
]