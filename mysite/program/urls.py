from django.urls import path
from . import views
from django.views import generic

urlpatterns = [
    path('', views.MyView.as_view(result='fffasdkgjasdfgkl;vrn'))
]