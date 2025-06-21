from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
from .views import UserViewSet
router = DefaultRouter() # amader router

router.register('list', views.DoctorViewset) # router er antena
router.register('designation', views.DesignationViewset) # router er antena
router.register('specialization', views.SpecializationViewset) # router er antena
router.register('available_time', views.AvailableTimeViewset) # router er antena
router.register('reviews', views.ReviewViewset, basename='reviews') # router er antena
router.register(r'users', UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
    # path('doctor/reviews/', views.ReviewViewset.as_view({'get': 'doctor_reviews'}), name='doctor-reviews'),
]