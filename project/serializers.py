from rest_framework import serializers
from .models import *


class Patserialiser(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields="__all__"

class Docserialiser(serializers.ModelSerializer):
    class Meta:
        model=Doctor
        fields="__all__"


class Sympserialiser(serializers.ModelSerializer):
    class Meta:
        model=Symptom
        fields="__all__"

class Disserialiser(serializers.ModelSerializer):
    class Meta:
        model=Disease
        fields="__all__"

class Transerialiser(serializers.ModelSerializer):
    class Meta:
        model=Transaction
        fields="__all__"

class Chatserialiser(serializers.ModelSerializer):
    class Meta:
        model=Chat
        fields="__all__"

class  Specserialiser(serializers.ModelSerializer):
    class Meta:
        model=Specialisation
        fields="__all__"

class Docserialiser(serializers.ModelSerializer):
    class Meta:
        model=Patient
        fields="__all__"


class Doc_specserialiser(serializers.ModelSerializer):
    class Meta:
        model=Doctor_specialisation
        fields="__all__"

class Qualserialiser(serializers.ModelSerializer):
    class Meta:
        model=Qualification
        fields="__all__"

class Hos_afflserialiser(serializers.ModelSerializer):
    class Meta:
        model=Hospital_affiliation
        fields="__all__"   

class Off_availabserialiser(serializers.ModelSerializer):
    class Meta:
        model=Office_doctor_available
        fields="__all__"


class Appserialiser(serializers.ModelSerializer):
    class Meta:
        model=Appointment
        fields="__all__"


class App_statusserialiser(serializers.ModelSerializer):
    class Meta:
        model=Appointment_status
        fields="__all__"                

