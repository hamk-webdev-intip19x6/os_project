# Generated by Django 3.0.2 on 2020-03-10 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rental_system', '0031_auto_20200310_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='work',
            name='date_added',
            field=models.DateField(auto_now=True),
        ),
    ]
