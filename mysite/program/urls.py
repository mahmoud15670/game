from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('user', views.UserView.as_view(), name='create_user'),
    path('user/<int:pk>', views.UserDetailView.as_view(), name='user_detail'),
    path('user/edit/<int:pk>', views.UpdateUserView.as_view(), name='edit'),
    path('user/delete/<int:pk>', views.UserDeleteView.as_view(), name='delete')
]