from rest_framework import serializers
from .models import Vaccine


class VaccineSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Vaccine
        fields = '__all__'

