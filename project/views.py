from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *

# Create your views here.

#The doctor view
def doctor(request):
    if request.method =='GET':
        doctor =Doctor.objects.all()
        serializer =Patserialiser(doctor,many=True)
    elif request.method == 'POST':
        serializer =Docserialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)        

    # elif request.method == 'PUT':
    #     serializer =Docserialiser(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=201)
    #     return Response(serializer.errors,status=400)    

    # elif request.method == 'DELETE':
    #     Docserialiser.delete()
        # serializer =Docserialiser(data=request.data)
        
        # serializer = Docserialiser.delete

    return Response(serializer.data)


#The patient view
@api_view(['GET','POST','PUT','DELETE'])
def patient(request,pk):
    try:
        patient=Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Response(status=404)    
    if request.method =='GET':
        patient =Patient.objects.all()
        serializer =Patserialiser(patient)
    elif request.method == 'POST':
        serializer =Patserialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

    # elif request.method == 'PUT':
    #     serializer =Patserialiser(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=201)
    #     return Response(serializer.errors,status=400)    

    # elif request.method == 'DELETE':
    #     Patserialiser.delete()
        # serializer =Docserialiser(data=request.data)
        
        # serializer = Docserialiser.delete

    return Response(serializer.data)


#The disease  view
# kakak
class ApiDisserialiser(APIView):
    def get(self, request):
        
        disease =Disease.objects.all()
        serializer =Disserialiser(disease,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer =Disserialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400) 

    def put(self, request):
        serializer =Disserialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)     


#The disease symptom views
class ApiSympserialiser(APIView):
    def get(self, request):
        symptom =Symptom.objects.all()
        serializer = Sympserialiser(symptom,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Sympserialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400) 




#The Transactions view
class ApiTranserialiser(APIView):
    def get(self, request):
        transaction =Transaction.objects.all()
        serializer =Transerialiser(transaction,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer =Transerialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400) 



#The Chats  view
class ApiChatserialiser(APIView):
    def get(self, request):
        chat =Chat.objects.all()
        serializer =Chatserialiser(chat,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer =Chatserialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400) 



#The doctor specialisation view
class ApiDoc_specserialiser(APIView):
    def get(self, request):
        doctor_specialisation =Doctor_specialisation.objects.all()
        serializer =Doc_specserialiser(doctor_specialisation,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer =Doc_specserialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400) 


# the 

class ApiDisserialiser(APIView):
    def get(self, request):
        disease =Disease.objects.all()
        serializer =Disserialiser(disease,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer =Disserialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)  




class ApiQualserialiser(APIView):
    def get(self, request):
        qualification =Qualification.objects.all()
        serializer =Qualserialiser(qualification,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer =Qualserialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)  



class ApiHos_afflserialiser(APIView):
    def get(self, request):
        hospital_affiliation =Hospital_affiliation.objects.all()
        serializer =Hos_afflserialiser(hospital_affiliation,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer =Hos_afflserialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)  


class ApiOff_availabserialiser(APIView):
    def get(self, request):
        office_doctor_available =Office_doctor_available.objects.all()
        serializer =off_availabserialiser(Office_doctor_available,many=True)
        return Response(serializer.data)

        serializer =Off_availabserialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)                  

# the appointment views
class ApiAppserialiser(APIView):
    def get(self, request):
        appointment =Appointment.objects.all()
        serializer =Appserialiser(appointment,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer =Appserialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)                  


# the appoinmet status view
class ApiApp_statusserialiser(APIView):
    def get(self, request):
        appointment_status =Appointment_status.objects.all()
        serializer =App_statusserialiser(appointment_status,many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer =App_statusserialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)                  







#the secuialisation view

class Apispecialiser(APIView):
    def get_object(self,id):
        try:
            return Specialisation.objects.get(id=id)

        except Specialisation.DoesNotExist:
            return Response(status=400)

    def get(self, request,id):
        specialisation =self.get_object(id)
        serializer =Specserialiser(specialisation)
        return Response(serializer.data)

    def post(self, request,id):
        serializer =Specserialiser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400) 

    def put(self, request,id):
        specialisation =self.get_object(id)
        serializer =Specserialiser(specialisation,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)         










# @api_view(['GET'])
# def one(request,pk):
#     doctor =Doctor.objects.get(pk=pk)
#     serializer =Docserialiser(doctor,many=False)
#     return Response(serializer.data)    

# @api_view(['POST'])
# def post_it(request):
#     serializer =Docserialiser(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,status=201)
#     return Response(serializer.errors,status=400) 


# @api_view(['DELETE'])
# def delete(request,pk):
#     serializer =Docserialiser(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,status=201)
#     return Response(serializer.errors,status=400)        
