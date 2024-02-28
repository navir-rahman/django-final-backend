from rest_framework import serializers
from .models import Vaccine
from django.utils import timezone
from user.models import DoctorModel


class VaccineSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Vaccine
        fields = '__all__'

class addVaccineSerializer(serializers.ModelSerializer ):
    initiated_by = serializers.StringRelatedField(many=False)
    class Meta:
        model = Vaccine
        fields = '__all__'

    def create(self, validated_data, user_instance=None):
        if user_instance is None:
            user_instance = self.context.get('user_instance')
            initiated_by = DoctorModel.objects.get(doctor = user_instance)
        print(user_instance)

        
        name = validated_data['name']
        image = validated_data['image']
        description = validated_data['description']
        dose_count = validated_data['dose_count']
        status = validated_data['status']
        campaign_name = validated_data['campaign_name']
        initiated_date = timezone.now().strftime('%Y-%m-%d')
            
        vaccineInstance = Vaccine.objects.create(name = name, image = image, description = description, dose_count = dose_count, status = status, campaign_name = campaign_name, initiated_date = initiated_date, initiated_by = initiated_by) 
        print(vaccineInstance)
        return False
    


# class VaccineRecordSerializer(serializers.ModelSerializer):
#     vaccine = serializers.StringRelatedField(many=False)
#     patient = serializers.StringRelatedField(many=False)

#     class Meta:
#         model = VaccineRecord
#         fields = '__all__'