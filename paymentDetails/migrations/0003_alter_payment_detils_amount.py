# Generated by Django 4.2 on 2023-07-22 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentDetails', '0002_alter_payment_detils_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_detils',
            name='amount',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
