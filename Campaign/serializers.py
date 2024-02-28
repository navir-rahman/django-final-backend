from rest_framework import serializers
from .models import Campaign
from Vaccine.models import Vaccine


class CampaignSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Campaign 
        fields = '__all__'

