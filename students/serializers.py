from rest_framework import serializers
from .models import Student
from sponsorship.serializers import SponsorshipSerializer
from sponsorship.models import Sponsorship
from django.db.models import Sum

class StudentSerializer(serializers.ModelSerializer):
    sponsor = SponsorshipSerializer(many=True, read_only=True, source="sponsorships")
    # otm=serializers.SerializerMethodField()
    amount_spent=serializers.SerializerMethodField()
    class Meta:
        model = Student
        fields = ['full_name', 'phone', 'type_of_student', 'sum_contract', 'otm', 'amount_spent', 'sponsor']



    def get_amount_spent(self, obj):
        total_received = Sponsorship.objects.filter(student=obj).aggregate(Sum('amount'))['amount__sum']
        return total_received or 0