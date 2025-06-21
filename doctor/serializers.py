from rest_framework import serializers
from . import models

class DoctorSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    specialization = serializers.StringRelatedField(many=True)
    designation = serializers.StringRelatedField(many=True)
    available_time = serializers.StringRelatedField(many=True)
    class Meta:
        model = models.Doctor
        fields = '__all__'

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = '__all__'

class DesignationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Designation
        fields = '__all__'

class AvailableTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AvailableTime
        fields = '__all__'

        
class ReviewSerializer(serializers.ModelSerializer):
    reviewer = serializers.SerializerMethodField()
    doctor = serializers.SerializerMethodField()
    
    class Meta:
        model = models.Review
        fields = '__all__'
    
    def get_reviewer(self, obj):
        return f"{obj.reviewer.user.first_name} {obj.reviewer.user.last_name}"
    
    def get_doctor(self, obj):
        return f"{obj.doctor.user.first_name} {obj.doctor.user.last_name}"