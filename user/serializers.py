from rest_framework import serializers
from .models import UserModel, PatientModel, DoctorModel
from django.contrib.auth.models import User

user_roles = (
    (1, 'doctor'),
    (2, 'patient'),
)


class UserSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = UserModel
        fields = '__all__'

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)



class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required = True)
    first_name = serializers.CharField(required = True)
    last_name = serializers.CharField(required = True)
    email = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
    confirm_password = serializers.CharField(required=True)
    past_medical_reports = serializers.CharField(required = True)
 

    class Meta:
        model = UserModel
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'nid', 'user_role', 'past_medical_reports', 'date_of_birth']
    
    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        nid = self.validated_data.get('nid')
        user_role = self.validated_data.get('user_role')
        past_medical_reports = self.validated_data.get('past_medical_reports')
        date_of_birth = self.validated_data.get('date_of_birth')
        
        if password != password2:
            raise serializers.ValidationError({'error': "Passwords don't match"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': "Email already exists"})
        
        # user = UserModel(username=username, email=email, first_name=first_name, last_name=last_name, nid=nid, user_role=user_role, past_medical_reports=past_medical_reports, date_of_birth=date_of_birth)
        user = User(username=username, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.is_active = False
        user.save()
        user_instance = UserModel.objects.create(account=user, nid=nid, user_role=user_role, date_of_birth=date_of_birth)
        if user_role == 'patient':
            PatientModel.objects.create(patient=user_instance,past_medical_reports=past_medical_reports)
        else:
            DoctorModel.objects.create(doctor=user_instance)
        return user_instance
