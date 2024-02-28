from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers



# Create your views here.
class VaccineRecordViewSet(viewsets.ModelViewSet):
    queryset  = models.VaccineRecord.objects.all()
    serializer_class = serializers.VaccineRecordSerializer




class order_vaccine(APIView):
    serializer_class = serializers.VaccineRecordSerializer
    def get(self, request, id):
        # user_token = request.GET.get('token')

        print(id)
        return Response({})

    def post(self, request, id):
        return Response({})
