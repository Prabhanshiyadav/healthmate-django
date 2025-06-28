from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db import models
from .models import Patient
from .forms import PatientForm

import csv
from django.http import HttpResponse

def export_patients_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="patients.csv"'

    writer = csv.writer(response)
    writer.writerow(['Name', 'Age', 'Contact', 'Diagnosis', 'Admission Date'])

    for patient in Patient.objects.all():
        writer.writerow([patient.name, patient.age, patient.contact, patient.diagnosis, patient.admission_date])

    return response

class PatientListView(ListView):
    model = Patient
    template_name = 'patients/patient_list.html'
    context_object_name = 'patients'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Patient.objects.filter(
                models.Q(name__icontains=query) | 
                models.Q(diagnosis__icontains=query)
            )
        return Patient.objects.all()


class PatientDetailView(DetailView):
    model = Patient
    template_name = 'patients/patient_detail.html'

from django.contrib import messages

class PatientCreateView(CreateView):
    model = Patient  # ✅ Required
    form_class = PatientForm
    template_name = 'patients/patient_form.html'
    success_url = reverse_lazy('patient_list')

    def form_valid(self, form):
        messages.success(self.request, "✅ Patient added successfully!")
        return super().form_valid(form)


class PatientUpdateView(UpdateView):
    ...
    def form_valid(self, form):
        messages.success(self.request, "✏️ Patient updated successfully!")
        return super().form_valid(form)

class PatientDeleteView(DeleteView):
    ...
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "🗑️ Patient deleted successfully.")
        return super().delete(request, *args, **kwargs)
