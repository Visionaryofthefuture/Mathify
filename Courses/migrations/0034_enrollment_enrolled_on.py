# Generated by Django 5.0.6 on 2024-07-09 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0033_enrollment'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrollment',
            name='enrolled_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]