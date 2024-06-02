from rest_framework import serializers

from . import models

class recordSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.records
        fields = ["date","details"]

class appointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.appointments
        fields = "__all__"

class patientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.patient
        fields = "__all__"

class hospitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.hospital
        fields = "__all__"