import django_filters
from students.models import Student, OTM

class StudentFilter(django_filters.FilterSet):
    otm = django_filters.ModelChoiceFilter(queryset=OTM.objects.all())

    class Meta:
        model = Student
        fields = ["type_of_student", "otm"]
