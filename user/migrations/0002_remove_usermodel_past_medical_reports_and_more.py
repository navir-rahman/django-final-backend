# Generated by Django 5.0.1 on 2024-02-17 04:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usermodel',
            name='past_medical_reports',
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='user_role',
            field=models.CharField(choices=[('doctor', 'Doctor'), ('patient', 'Patient')], max_length=20),
        ),
        migrations.CreateModel(
            name='PatientModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('past_medical_reports', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='user.usermodel')),
            ],
        ),
    ]
