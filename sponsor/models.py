from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from students.models import validate_phone_length

class Sponsor(models.Model):
    STATUS = [
       ('Yangi', 'Yangi'),
       ('Moderatsiyada', 'Moderatsiyada'),
       ('Tasdiqlangan', 'Tasdiqlangan'),
       ('Bekor qilingan', 'Bekor qilingan'),
    ]

    SPONSOR_TYPE_CHOICES = [
        ('Jismoniy shaxs', 'Jismoniy shaxs'),
        ('Yuridik shaxs', 'Yuridik shaxs'),
    ]
    type_payment_choice=[
        ('Pul o`tkazmalari', 'Pul o`tkazmalari'),
    ]

    full_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Ф.И.О')
    phone = models.CharField(max_length=9, unique=True, blank=True, null=True, verbose_name='Телефон номер', validators=[validate_phone_length])
    sponsorship = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, db_index=True, verbose_name='Сумма спонсора')
    date = models.DateTimeField(default=timezone.now, db_index=True)
    sponsor_type = models.CharField(max_length=15, choices=SPONSOR_TYPE_CHOICES, default='Jismoniy shaxs')
    status = models.CharField(max_length=100, choices=STATUS, default='Yangi', db_index=True, verbose_name='Статус')
    type_payment=models.CharField(max_length=100, choices=type_payment_choice, default='Pul o`tkazmalari', verbose_name='Тип перевода')
    company_name = models.CharField(max_length=255, blank=True, null=True, verbose_name='Название компании')
    # linkdetail=models.URLField(blank=True, null=True, verbose_name='Подробнее')

    class Meta:
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['date']),
            models.Index(fields=['sponsorship']),
        ]
        verbose_name = 'Sponsor'
        verbose_name_plural = 'Sponsors'

    def clean(self):

        if self.sponsor_type == 'Yuridik shaxs' and not self.company_name:
            raise ValidationError({'company_name': 'Название компании обязательно для юридического лица.'})
        if self.sponsor_type == 'Jismoniy shaxs' and self.company_name:
            raise ValidationError({'company_name': 'Физическое лицо не может иметь название компании.'})

    @property
    def is_company(self):
        return self.sponsor_type == 'Yuridik shaxs'

    @property
    def display_name(self):
        return self.company_name if self.is_company else self.full_name

    def __str__(self):
        return f"{self.display_name} ({self.full_name})" if self.is_company else self.full_name
