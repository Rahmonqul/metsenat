from django.db import models

# Create your models here.

class Sponsorship(models.Model):
    STATUS = [
       ('Yangi', 'Yangi'),
       ('Moderatsiyada', 'Moderatsiyada'),
       ('Tasdiqlangan', 'Tasdiqlangan'),
       ('Bekor qilingan', 'Bekor qilingan'),
    ]
    sponsor = models.ForeignKey("sponsor.Sponsor", on_delete=models.CASCADE, related_name="sponsorships",
                                verbose_name="Спонсор")
    student = models.ForeignKey("students.Student", on_delete=models.CASCADE, null=True, blank=True, related_name="sponsorships",
                                verbose_name="Студент")
    amount = models.DecimalField(max_digits=15, decimal_places=2, verbose_name="Сумма поддержки")
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата перевода")

    class Meta:
        verbose_name = "Sponsorship"
        verbose_name_plural = "Sponsorships"


    def __str__(self):
        return f"{self.sponsor.full_name} → {self.student.full_name} ({self.amount} сум)"

