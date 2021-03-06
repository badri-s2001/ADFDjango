# Generated by Django 3.2.7 on 2021-09-15 06:06

from django.db import migrations, models
import django.utils.datetime_safe


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField(default=django.utils.datetime_safe.date.today)),
                ('gender', models.CharField(max_length=10)),
                ('nationality', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('pincode', models.IntegerField()),
                ('qualification', models.CharField(max_length=20)),
                ('salary', models.IntegerField()),
                ('pan_number', models.CharField(max_length=20)),
            ],
        ),
        migrations.DeleteModel(
            name='Response',
        ),
    ]
