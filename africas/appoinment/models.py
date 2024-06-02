from django.db import models

# Create your models here.
class patient(models.Model):
    name = models.CharField(max_length=10000)
    location = models.CharField(max_length=10000)
    phone_no = models.IntegerField()
    age = models.IntegerField()
    id_no = models.IntegerField()

class hospital(models.Model):
    name = models.CharField(max_length=100000)
    location = models.CharField(max_length=100000)
    doctor = models.CharField(max_length=10000)

class appointments(models.Model):
    patient = models.ForeignKey(patient,on_delete=models.CASCADE)
    date = models.DateTimeField()
    hospital = models.ForeignKey(hospital,on_delete=models.CASCADE)

class records(models.Model):
    patient = models.ForeignKey(patient,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    details = models.TextField()

class reports(models.Model):
    details = models.CharField(max_length=100000)