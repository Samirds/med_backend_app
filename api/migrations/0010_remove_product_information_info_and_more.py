# Generated by Django 4.2 on 2023-09-19 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_remove_product_information_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_information',
            name='info',
        ),
        migrations.AddField(
            model_name='product_information',
            name='image',
            field=models.ImageField(blank=True, max_length=250, null=True, upload_to='Images'),
        ),
        migrations.AlterField(
            model_name='product_information',
            name='description',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]