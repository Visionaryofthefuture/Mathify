# Generated by Django 5.0.6 on 2024-07-02 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('Instructor', 'Instructor')], max_length=11),
        ),
    ]