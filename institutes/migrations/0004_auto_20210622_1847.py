# Generated by Django 3.2.1 on 2021-06-22 13:17

from django.db import migrations, models
import institutes.models


class Migration(migrations.Migration):

    dependencies = [
        ('institutes', '0003_auto_20210615_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_pic',
            field=models.ImageField(null=True, upload_to=institutes.models.Course.get_file_upload_path),
        ),
        migrations.AlterField(
            model_name='course',
            name='syllabus',
            field=models.FileField(null=True, upload_to=institutes.models.Course.get_file_upload_path),
        ),
    ]
