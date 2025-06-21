from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework import filters, pagination
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.permissions import BasePermission
from rest_framework.decorators import action # add this new
from rest_framework.response import Response # add this new


class SpecializationViewset(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.SpecializationSerializer

class DesignationViewset(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DesignationSerializer

class AvailableTimeForSpecificDoctor(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        doctor_id = request.query_params.get('doctor_id')
        if doctor_id:
            return queryset.filter(doctor=doctor_id)
        return queryset

class AvailableTimeViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.AvailableTimeSerializer
    filter_backends=[AvailableTimeForSpecificDoctor]

class DoctorPagination(pagination.PageNumberPagination):
    page_size = 1
    page_size_query_param = 'page_size'
    max_page_size = 100

class DoctorViewset(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = DoctorPagination
    search_fields = ['user__first_name', 'user__email', 'specialization__name', 'designation__name']


# class ReviewViewset(viewsets.ModelViewSet):
#     queryset = models.Review.objects.all()
#     serializer_class = serializers.ReviewSerializer

class ReviewViewset(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    
    def get_queryset(self):
        queryset = super().get_queryset()
        doctor_id = self.request.query_params.get('doctor_id')
        if doctor_id:
            queryset = queryset.filter(doctor_id=doctor_id)
        return queryset
    
    # OR alternatively, you can add a custom endpoint:
    @action(detail=False, methods=['get'])
    def by_doctor(self, request):
        doctor_id = request.query_params.get('doctor_id')
        if not doctor_id:
            return Response({"error": "doctor_id parameter is required"}, status=400)
        
        reviews = models.Review.objects.filter(doctor_id=doctor_id)
        serializer = self.get_serializer(reviews, many=True)
        return Response(serializer.data)