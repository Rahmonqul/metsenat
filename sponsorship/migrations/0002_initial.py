# Generated by Django 5.1.6 on 2025-02-07 06:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sponsorship', '0001_initial'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsorship',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sponsorships', to='students.student', verbose_name='Студент'),
        ),
    ]
