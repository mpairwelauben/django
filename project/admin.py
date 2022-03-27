from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Specialisation)
admin.site.register(Doctor_specialisation)
admin.site.register(Appointment)
admin.site.register(Qualification)
admin.site.register(Hospital_affiliation)
admin.site.register(Office)
admin.site.register(Office_doctor_available)
admin.site.register(Appointment_status)
admin.site.register(Disease)
admin.site.register(Chat)
admin.site.register(Symptom)
admin.site.register(Transaction)