# Generated by Django 4.2 on 2023-04-26 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_product_information_advertisable_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_information',
            name='image',
            field=models.FileField(blank=True, max_length=250, null=True, upload_to='Images/'),
        ),
    ]
