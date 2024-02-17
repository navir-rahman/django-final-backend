# Generated by Django 5.0.1 on 2024-02-17 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vaccine', '0001_initial'),
        ('user', '0004_doctormodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctormodel',
            name='vaccines',
            field=models.ManyToManyField(blank=True, default=None, related_name='vaccines', to='Vaccine.vaccine'),
        ),
    ]
