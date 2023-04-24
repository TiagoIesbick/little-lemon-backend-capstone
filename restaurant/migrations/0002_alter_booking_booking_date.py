# Generated by Django 4.2 on 2023-04-24 23:06

from django.db import migrations, models
import restaurant.validators


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateTimeField(validators=[restaurant.validators.validate_date]),
        ),
    ]