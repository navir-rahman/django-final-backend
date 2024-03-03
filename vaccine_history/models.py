from django.db import models
from Vaccine.models import Vaccine
from user.models import PatientModel
from django.utils import timezone

# Create your models here.
class VaccineRecord(models.Model):
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    patient = models.ForeignKey(PatientModel, on_delete=models.CASCADE)
    date_taken = models.DateField(default=timezone.now)

    def __str__(self):
        return self.vaccine.name
    

