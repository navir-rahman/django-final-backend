from django.shortcuts import redirect
from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from . import models
from . import serializers
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes

from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token as AuthToken
from user.models import UserModel

from rest_framework.generics import DestroyAPIView, UpdateAPIView
# Create your views here.
class VaccineViewSet(viewsets.ModelViewSet):
    queryset  = models.Vaccine.objects.all()
    serializer_class = serializers.VaccineSerializer



class AddVaccineViewSet(APIView):
    def get(self, request):
        return Response({})
    
    def post(self, request):
        # token 
        
        token_key = request.headers.get('Authorization')
        parts = token_key.split()
        if len(parts) == 2 and parts[0].lower() == 'bearer':
            received_token = parts[1]
        auth_token_instance = AuthToken.objects.get(key=received_token)
        # print(received_token, auth_token_instance)
        token = Token.objects.get(key=auth_token_instance)
        user_instance = UserModel.objects.get(account = token.user)
        # print(initiated_by)

        serializer = serializers.addVaccineSerializer(data=request.data, context={'user_instance': user_instance})
        if serializer.is_valid():
           serializer.save()
            
        return Response(serializer.errors)
    


# views.py

class VaccineDeleteAPIView(DestroyAPIView):
    queryset = models.Vaccine.objects.all()
    serializer_class = serializers.addVaccineSerializer
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'status':'OK'})

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)







# Create your views here.
# class VaccineRecordViewSet(viewsets.ModelViewSet):
#     queryset  = models.VaccineRecord.objects.all()
#     serializer_class = serializers.VaccineRecordSerializer




# class order_vaccine(APIView):
#     def get(self, request, id):
#         # Extract user information from the token
#         user_token = request.GET.get('token')

#         print(id)
#         return Response({"success": "Vaccine record created successfully"}, status=status.HTTP_201_CREATED)

from rest_framework import status
from rest_framework.decorators import api_view



@api_view(['GET', 'PATCH'])
def vaccine_detail(request, pk):
    try:
        vaccine_instance = models.Vaccine.objects.get(pk=pk)
    except models.Vaccine.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = serializers.VaccineSerializer(vaccine_instance)
        return Response(serializer.data)

    elif request.method == 'PATCH':
        serializer = serializers.VaccineSerializer(vaccine_instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)