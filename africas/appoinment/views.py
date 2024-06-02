from django.shortcuts import render
# from rest_framework import *
from . import serializer
from . import models
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


# Create your views here.
@csrf_exempt
def index(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        session_code = request.POST.get('serviceCode')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        patient = get_object_or_404(models.patient, phone_no=phone_number)
        response = ""

        if text == "":
            response = "CON Karibu Afya Bora! \n Which service would you like to access? \n \n"
            response += "1. View my records \n"
            response += "2. Hospital appointment \n"
            response += "3. Nearest hospital \n"
            response += "4. Emergency services \n"
            response += "5. Report an issue"

        elif text == "1":
            record = models.records.objects.filter(patient=patient)
            record = serializer.recordSerializer(record,many=True).data
            response = f"END {record}"

        elif text == "2":
            response = "CON Choose an option \n"
            response += "1. View Appointment\n"
            response += "2. Book an appointment\n"
            response += "3. Cancel appointment"

        elif text == '2*1':
            data = models.appointments.objects.filter(patient=patient)
            apps = serializer.appointmentSerializer(data,many=True).data
            #for i in apps:
            response += f"END You're booked appointment is on Friday 31st May 2024"
   
        elif text == '2*2':

            data = models.appointments.objects.all().filter(patient=patient).delete()
            response = f"END Appointment booked"

        elif text == '2*3':
            data = models.appointments.objects.all().filter(patient=patient).delete()
            response = f"END Appointment canceled"

        elif text == '3':
            l = serializer.patientSerializer(patient).data
            location = l["location"]
            near_hospitals = models.hospital.objects.filter(location=location)
            hospitals = serializer.hospitalSerializer(near_hospitals,many=True).data
            for i in hospitals:
                # print(i['name'],i['location'])
            
                response = f"END {i['name']} {i['location']}"
        elif text == '4':
            response += "END Here is a list of emergency services contacts:\n"
            response += "1. Kenya Red Cross : 0700395395\n"
            response += "2. St. John's Ambulance: 0721611555 \n"
            response += "3. Nairobi Fire Emergency Services : 0202344599\n"
            response += "4. Central Police : 0736350100 \n"
            # response += "END hospital services : 075432156"

        elif text == '5':
            response = "CON Explain your problem in detail \n"
        
        elif text.startswith('5*'):
            t = text.split('*')[1].strip()
            new = models.reports.objects.create(details = t)
            # new.save()
            response = "END Your report has been submitted"
        return HttpResponse(response)
class BookAppointment():
    pass    

class Records():
    pass

class Register():
    pass