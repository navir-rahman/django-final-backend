from rest_framework import viewsets
from .models import Vaccine
from . import serializers
# Create your views here.
class VaccineViewSet(viewsets.ModelViewSet):
    queryset  = Vaccine.objects.all()
    serializer_class = serializers.VaccineSerializer

