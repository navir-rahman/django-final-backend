# Generated by Django 5.0.1 on 2024-02-22 13:35

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vaccine', '0005_vaccine_image'),
        ('user', '0008_remove_doctormodel_campaign'),
    ]

    operations = [
        migrations.AddField(
            model_name='vaccine',
            name='campaign_name',
            field=models.CharField(blank=True, default='2024-02-22', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='vaccine',
            name='initiated_by',
            field=models.ForeignKey(blank=True, default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.doctormodel'),
        ),
        migrations.AddField(
            model_name='vaccine',
            name='initiated_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='vaccine',
            name='status',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]