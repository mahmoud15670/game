from django.urls import path

from . import views

urlpatterns = [
     path('', views.IndexView.as_view(), name='index'),
     path('patient', views.PatientCreateView.as_view(), name='create_patient'),
     path('patient/<int:pk>', views.PatientDetilView.as_view(), name='patient_detil'),
     path('patient/edit/<int:pk>',views.PatientEditView.as_view(), name='patient_edit'),
     path('patient/delete/<int:pk>',views.PatientDeleteView.as_view(), name='patient_delete'),
     path('tests', views.TestListView.as_view(), name='test_list'),
     path('test', views.TestCreateView.as_view(), name='create_test'),
     path('test/<int:pk>', views.TestDetilView.as_view(), name='test_detil'),
     path('test/edit/<int:pk>', views.TestEditView.as_view(), name='test_edit'),
     path('test/delete/<int:pk>', views.TestDeleteView.as_view(), name='test_delete'),
]
