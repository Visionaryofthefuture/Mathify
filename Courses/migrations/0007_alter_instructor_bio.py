# Generated by Django 5.0.6 on 2024-07-02 05:12

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0006_instructor_review_section_lecture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instructor',
            name='bio',
            field=django_ckeditor_5.fields.CKEditor5Field(default='text', verbose_name='Text'),
        ),
    ]