# Generated by Django 5.0.6 on 2024-07-09 08:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0036_rename_lesson_section'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('video', models.FileField(blank=True, null=True, upload_to='videos/')),
                ('youtube_url', models.URLField(blank=True, null=True)),
                ('content', models.TextField(blank=True, null=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='Courses.section')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
