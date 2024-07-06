# Generated by Django 5.0.6 on 2024-07-05 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0013_auto_20240705_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='Instructor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='User', to='Courses.instructor'),
        ),
    ]