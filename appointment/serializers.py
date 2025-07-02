from rest_framework import serializers
from .import models
from doctor.models import AvailableTime

class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvailableTime
        fields = ['name']  # Adjust according to your model field

class AppointmentSerializer(serializers.ModelSerializer):
    # time = serializers.StringRelatedField(many =False)
    # doctor = serializers.StringRelatedField(many = False)
    # patient = serializers.StringRelatedField(many = False)
    time_detail = AvailableTimeSerializer(source='time', read_only=True) 
    class Meta:
        model = models.Appointment
        fields = '__all__'