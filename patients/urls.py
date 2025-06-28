from django.urls import path
from .views import (
    PatientListView,
    PatientDetailView,
    PatientCreateView,
    PatientUpdateView,
    PatientDeleteView,
    export_patients_csv,
)

urlpatterns = [
    path('', PatientListView.as_view(), name='patient_list'),
    path('patient/<int:pk>/', PatientDetailView.as_view(), name='patient_detail'),
    path('add/', PatientCreateView.as_view(), name='patient_add'),
    path('edit/<int:pk>/', PatientUpdateView.as_view(), name='patient_edit'),
    path('delete/<int:pk>/', PatientDeleteView.as_view(), name='patient_delete'),
    path('export/', export_patients_csv, name='export_patients'),
]
