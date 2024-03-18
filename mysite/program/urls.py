from django.urls import path
from . import views
from django.views import View

urlpatterns=[
    path('', View.as_view())
]