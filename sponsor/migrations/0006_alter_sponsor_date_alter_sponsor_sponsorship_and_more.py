# Generated by Django 5.1.6 on 2025-02-08 06:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sponsor', '0005_alter_sponsor_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='date',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='sponsorship',
            field=models.DecimalField(db_index=True, decimal_places=2, default=0.0, max_digits=15, verbose_name='Сумма спонсора'),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='status',
            field=models.CharField(choices=[('Yangi', 'Yangi'), ('Moderatsiyada', 'Moderatsiyada'), ('Tasdiqlangan', 'Tasdiqlangan'), ('Bekor qilingan', 'Bekor qilingan')], db_index=True, default='Yangi', max_length=100, verbose_name='Статус'),
        ),
        migrations.AddIndex(
            model_name='sponsor',
            index=models.Index(fields=['status'], name='sponsor_spo_status_203b37_idx'),
        ),
        migrations.AddIndex(
            model_name='sponsor',
            index=models.Index(fields=['date'], name='sponsor_spo_date_7b5ed4_idx'),
        ),
        migrations.AddIndex(
            model_name='sponsor',
            index=models.Index(fields=['sponsorship'], name='sponsor_spo_sponsor_06a54c_idx'),
        ),
    ]
