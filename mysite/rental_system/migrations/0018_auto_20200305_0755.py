# Generated by Django 3.0.2 on 2020-03-05 05:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_system', '0017_rentedwork_date_returned'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='pub_date',
            field=models.IntegerField(default=2020, validators=[django.core.validators.MaxValueValidator(2020), django.core.validators.MinValueValidator(1800)]),
        ),
    ]
