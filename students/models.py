from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError

def validate_phone_length(value):
    if not value.isdigit():
        raise ValidationError("Номер телефона должен содержать только цифры.")
    if len(value) != 9:
        raise ValidationError("Номер телефона должен содержать ровно 9 цифр (пример: 991234567).")



class OTM(models.Model):
    name_universitet = models.CharField(max_length=200, blank=True, null=True, verbose_name='Имя учебного заведения')

    def __str__(self):
        return self.name_universitet


class Student(models.Model):
    TYPE_OF_STUDENT_CHOICES = [
        ('Kolledj', 'Kolledj'),
        ('Bakalavr', 'Bakalavr'),
        ('Magistratura', 'Magistratura'),
    ]

    full_name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Ф.И.О')
    phone = models.CharField(max_length=9, unique=True, blank=True, null=True, db_index=True, verbose_name='Телефон номер', validators=[validate_phone_length])
    otm = models.ForeignKey(OTM, on_delete=models.CASCADE, blank=True, null=True, db_index=True, verbose_name='Учебное заведение')
    type_of_student = models.CharField(max_length=200, choices=TYPE_OF_STUDENT_CHOICES, blank=True, db_index=True, null=True, verbose_name='Тип обучения')
    sum_contract = models.DecimalField(max_digits=15, decimal_places=2, default=0.00, verbose_name='Сумма контракта')
    sponsors = models.ManyToManyField('sponsor.Sponsor', through='sponsorship.Sponsorship', related_name='students', verbose_name="Спонсоры")
    date = models.DateTimeField(default=timezone.now)
    class Meta:
        indexes = [
            models.Index(fields=['phone']),
            models.Index(fields=['otm']),
            models.Index(fields=['type_of_student']),
        ]
        verbose_name = "Student"
        verbose_name_plural = 'Students'

    def __str__(self):
        return self.full_name

