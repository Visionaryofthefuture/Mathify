# Generated by Django 5.0.6 on 2024-07-06 08:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0031_alter_course_instructor_delete_instructor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='Courses.category'),
        ),
    ]
