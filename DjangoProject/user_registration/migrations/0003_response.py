# Generated by Django 3.2.7 on 2021-09-15 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0002_auto_20210915_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.IntegerField()),
                ('response', models.CharField(max_length=20)),
                ('reason', models.CharField(max_length=500)),
            ],
        ),
    ]
