from django.contrib import admin
from .models import UserModel, PatientModel, DoctorModel
# Register your models here.
admin.site.register(UserModel) 
admin.site.register(PatientModel) 
admin.site.register(DoctorModel)  