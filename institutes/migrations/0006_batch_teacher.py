# Generated by Django 3.2.1 on 2021-06-30 13:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0003_auto_20210630_1900'),
        ('institutes', '0005_batch'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teachers.teacher'),
        ),
    ]
