
import django_filters
from .models import Sponsor


STATUS_CHOICES = [
    ("Barchasi", "Barchasi"),
    ("Yangi", "Yangi"),
    ("Moderatsiyada", "Moderatsiyada"),
    ("Tasdiqlangan", "Tasdiqlangan"),
    ("Bekor qilingan", "Bekor qilingan"),
]

class SponsorFilter(django_filters.FilterSet):
    sponsorship = django_filters.NumberFilter(field_name="sponsorship", lookup_expr="exact")
    date = django_filters.DateFromToRangeFilter(field_name="date")
    status = django_filters.ChoiceFilter(field_name="status", choices=STATUS_CHOICES, method="filter_status")

    def filter_status(self, queryset, name, value):
        if value == "Barchasi":
            return queryset
        return queryset.filter(status=value)

    class Meta:
        model = Sponsor
        fields = ["sponsorship", "date", "status"]