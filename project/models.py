from django.db import models
from django.utils import timezone
import datetime

# # Create your models here.
# The below section talks about the diseae, its symptoms and the category of the disease it belngs in
class Patient(models.Model):
    name =models.CharField(max_length=200,null=False)
    contact_number =models.IntegerField(null=False)
    email =models.CharField(max_length=200,null=False)
    location =models.CharField(max_length=200,null=False)
    age =models.IntegerField(null=False)

    def __str__(self):
        return str(self.name) 

class Doctor(models.Model):
    name =models.CharField(max_length=200,null=False)
    porfessional_stamement =models.CharField(max_length=200,null=False)
    practicing_from =models.DateTimeField(auto_now_add=True)
    email =models.CharField(max_length=200,null=False)
    location =models.CharField(max_length=200,null=False)
    
    def __str__(self):
        return str(self.name)         

class Symptom(models.Model):
   name =models.CharField(max_length=200, null=False)
   
   def __str__(self):
       return str(self.name)


class Disease(models.Model):
    disease_name=models.CharField(max_length=200, null=False)
    patient_name=models.ForeignKey(Patient,null=True, on_delete=models.SET_NULL)
    doctor=models.ForeignKey(Doctor,null=True, on_delete=models.SET_NULL)
    tags=models.ManyToManyField(Symptom)

    def __str__(self):
        return str(self.disease_name)


class Chat(models.Model):
    chat_name=models.CharField(max_length=200, null=False)
    # patient_name=models.ForeignKey(Patient,null=True, on_delete=models.SET_NULL)
    # doctor=models.ForeignKey(Doctor,null=True, on_delete=models.SET_NULL)
    message =models.TextField(null=False,max_length=200)
  

    def __str__(self):
        return str(self.chat_name)         


class Transaction(models.Model):
    name =models.CharField(max_length=200, null=False)
    patient=models.ForeignKey(Patient,null=True, on_delete=models.SET_NULL)
    doctor=models.ForeignKey(Doctor,null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return str(self.name)
        
    #   THIS PAGE SHOWS THE MODELS FOR THE DOCTORS PART             


class Specialisation(models.Model):
    name =models.CharField(max_length=200,null=False)
    
    def __str__(self):
        return str(self.name) 


class Doctor_specialisation(models.Model):
    doctor =models.ForeignKey(Doctor,on_delete=models.SET_NULL,null=True)
    # specialisation_id =models.ForeignKey(Specialisation, on_delete=models.SET_NULL,null=True)
    porfessional_stamement =models.CharField(max_length=200,null=False)
    practicing_from =models.DateTimeField(auto_now_add=True)
    tags=models.ManyToManyField(Specialisation)

    def __str__(self):
        return str(self.doctor) 

class Qualification(models.Model):
    doctor =models.ForeignKey(Doctor, on_delete=models.SET_NULL,null=True)
    qualification_name =models.CharField(max_length=200,null=False)
    institute_name =models.CharField(max_length=200,null=False)
    procurement_year =models.DateTimeField(auto_now_add=True)
    # practicing_from =models.DateTimeField()

    def __str__(self):
        return str(self.qualification_name) 



class Hospital_affiliation(models.Model):
    hospital_affiliated_name =models.CharField(max_length=200,null=False)
    Location =models.CharField(max_length=200,null=False)
    doctor=models.ForeignKey(Doctor, on_delete=models.SET_NULL,null=True)
    start_date =models.DateTimeField(auto_now_add=True)
    #auo_add_now adds timestamos
    end_date =models.DateTimeField(auto_now_add=True)
    practicing_from =models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.hospital_affiliated_name) 


# THESE NEXT MODELS CLEARLY IDENTIFY AND TALK ABOUT TE AREA OF OFFICE OF THE DOCTOR AND 
# THEIR AVAILABILITY

class Office(models.Model):
    office_name =models.CharField(max_length=200)
    doctor =models.ForeignKey(Doctor, on_delete=models.SET_NULL,null=True)
    hospital_affiliation_id =models.ForeignKey(Hospital_affiliation, on_delete=models.SET_NULL,null=True)
    Location =models.CharField(max_length=200,null=False)
    time_allocation_in_minutes =models.IntegerField(null=False)
    first_time_consultation_fee =models.IntegerField(null=False)
    followup_consultation_fee =models.IntegerField(null=False)
    
    def __str__(self):
        return str(self.office_name) 

class Office_doctor_available(models.Model):
    office=models.ForeignKey(Office, on_delete=models.SET_NULL,null=True)
    # day_of_the_week =models.ForeignKey(Hospital_affiliation, on_delete=models.SET_NULL,null=True)
    start_time =models.DateTimeField(auto_now_add=True,blank=True)
    end_time =models.DateTimeField(auto_now_add=True,blank=True)
    is_available =models.BooleanField(default=False,null=False)
    reason_of_unavailable =models.TextField(max_length=200,null=False)

    def __str__(self):
        return str(self.office.doctor.name) 


# THE FOLLOWING TABLES IDENTIFY AND SHOW THE  CLIENT/PATIET INFORMATION AS LISTEB BELOW 



# THE FOLLOWING MODEL WILL INDICATE DATABASEES TO THE APPOITMENT REARED FIELDS    

class Appointment_status(models.Model):
   status  =models.CharField(max_length=200,null=False)

   def __str__(self):
        return str(self.status) 

class Appointment(models.Model):
    day_of_the_week=(
        ("monday","monday"),
        ("Tuesday","Tuesday"),
        ("Wednesday","Wednesday"),
        ("Thursday","Thursday"),
        ("Friday","Friday"),
        ("Satuarday","Satuarday"),
        ("Sunday","Sunday"),
    )
    doctor =models.ForeignKey(Doctor,on_delete=models.SET_NULL,null=True)
    office =models.ForeignKey(Office, on_delete=models.SET_NULL,null=True)
    patient=models.ForeignKey(Patient, on_delete=models.SET_NULL,null=True)
    appointment_on =models.CharField(max_length=200,choices=day_of_the_week)
    probable_start_time =models.DateTimeField(auto_now_add=True)
    actual_end_time =models.DateTimeField(auto_now_add=True)
    appointment_status =models.ForeignKey(Appointment_status, on_delete=models.SET_NULL,null=True)
    appointment_taken_date =models.DateField()
    
    def __str__(self):
        print ("appointment")
        return str(self.id) 

