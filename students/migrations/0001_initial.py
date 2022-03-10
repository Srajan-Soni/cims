# Generated by Django 3.2.1 on 2021-07-25 12:24

from django.db import migrations, models
import django.db.models.deletion
import students.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('contact', models.CharField(max_length=10)),
                ('activation_code', models.CharField(max_length=20, null=True)),
                ('about_me', models.CharField(max_length=500, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('dob', models.DateField(null=True)),
                ('profile_pic', models.ImageField(null=True, upload_to=students.models.Student.get_upload_path)),
                ('gender', models.BooleanField(null=True)),
                ('city', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.city')),
                ('status', models.ForeignKey(default=2, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.status')),
            ],
            options={
                'db_table': 'students',
            },
        ),
    ]