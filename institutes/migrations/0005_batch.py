# Generated by Django 3.2.1 on 2021-06-30 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
        ('institutes', '0004_auto_20210622_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=50)),
                ('mode', models.BooleanField()),
                ('frequency', models.BooleanField()),
                ('start_date', models.DateField()),
                ('duration', models.PositiveIntegerField()),
                ('start_time', models.TimeField()),
                ('student_count', models.IntegerField(default=0)),
                ('course_fees', models.PositiveIntegerField()),
                ('concession', models.PositiveIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institutes.course')),
                ('status', models.ForeignKey(default=4, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.status')),
            ],
            options={
                'db_table': 'batches',
            },
        ),
    ]