from rest_framework import serializers
from .models import VaccineRecord
from django.utils import timezone
from user.models import DoctorModel






class VaccineRecordSerializer(serializers.ModelSerializer):
    # vaccine = serializers.StringRelatedField(many=False)
    # patient = serializers.StringRelatedField(many=False)

    class Meta:
        model = VaccineRecord
        fields = '__all__'