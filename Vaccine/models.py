from django.db import models
# from user.models import DoctorModel
# Create your models here.
status = ( 
    ('active', 'active'),
    ('complete', 'complete'),
    ('continuous', 'continuous'),
)
class Vaccine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    dose_count = models.IntegerField(default= 3, null=True, blank=True)
    # initiated_by = models.ForeignKey(DoctorModel, on_delete=models.CASCADE)
    status = models.BooleanField(default=False, null=True)

    def __str__(self) -> str:
        return self.name
