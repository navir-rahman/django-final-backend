from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    nid = models.IntegerField()
    past_medical_reports = models.TextField()
    # past_vaccines = models.TextField()

    # Add more fields as needed

    def __str__(self):
        return self.account.username
