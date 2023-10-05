# Generated by Django 4.2 on 2023-07-11 18:25

import ImageUploader.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ImageUploader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prescriptionimage',
            name='Username',
            field=models.CharField(default='sam', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='prescriptionimage',
            name='image',
            field=models.ImageField(max_length=250, upload_to=ImageUploader.models.PrescriptionImage.nameFile),
        ),
    ]
