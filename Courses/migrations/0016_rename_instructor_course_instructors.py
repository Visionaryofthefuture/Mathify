# Generated by Django 5.0.6 on 2024-07-05 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0015_alter_lecture_options_alter_section_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Instructor',
            new_name='Instructors',
        ),
    ]