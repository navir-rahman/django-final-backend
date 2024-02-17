from django.db import models
from Vaccine.models import Vaccine

# Create your models here.
class Campaign(models.Model):
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE, default = None, null=True, blank=True)
    campaign_name = models.CharField(max_length=20)
    initiated_date = models.DateTimeField(auto_now_add=True)
    description  = models.TextField()

    def __str__(self) -> str:
        return 

