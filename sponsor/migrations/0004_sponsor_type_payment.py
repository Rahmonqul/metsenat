# Generated by Django 5.1.6 on 2025-02-07 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0003_sponsor_status_alter_sponsor_company_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='type_payment',
            field=models.CharField(choices=[('Pul o`tkazmalari', 'Pul o`tkazmalari')], default='Pul o`tkazmalari', max_length=100, verbose_name='Тип перевода'),
        ),
    ]
