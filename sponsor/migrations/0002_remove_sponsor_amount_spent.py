# Generated by Django 5.1.6 on 2025-02-07 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='amount_spent',
        ),
    ]
