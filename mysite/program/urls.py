from django.urls import path
from . import views
from django.views import generic

urlpatterns = [
    path('', generic.View.as_view())
]