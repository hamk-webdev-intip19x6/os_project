# Generated by Django 3.0.2 on 2020-02-18 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('desc', models.CharField(max_length=200)),
                ('pub_date', models.DateField()),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental_system.Type')),
            ],
        ),
        migrations.CreateModel(
            name='Creator_Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental_system.Creator')),
                ('work_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental_system.Work')),
            ],
        ),
    ]
