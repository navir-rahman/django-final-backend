from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()
router.register('all_vaccine', views.VaccineViewSet) 
urlpatterns = [
    path('', include(router.urls)),
    
]