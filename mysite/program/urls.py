from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserView.as_view(), name='user'),
    path('user/<int:pk>', views.UpdateUserView.as_view(), name='edit')
]