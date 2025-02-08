from rest_framework import serializers
from sponsor.models import Sponsor
from .models import Sponsorship
from students.models import Student
from django.db.models import Sum


class SponsorshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsorship
        fields = ['sponsor', 'amount']

    def validate(self, data):
        sponsor = data['sponsor']
        amount = data['amount']

        if amount > sponsor.sponsorship:
            raise serializers.ValidationError(
                {"amount": "Сумма не может превышать сумму спонсорства."}
            )
        return data



class SummarySerializer(serializers.Serializer):
    total_sponsorship_amount = serializers.SerializerMethodField()
    total_student_contract_amount = serializers.SerializerMethodField()
    remaining_amount = serializers.SerializerMethodField()

    def get_total_sponsorship_amount(self, obj):
        return Sponsorship.objects.aggregate(total=Sum('amount'))['total'] or 0

    def get_total_student_contract_amount(self, obj):
        return Student.objects.aggregate(total=Sum('sum_contract'))['total'] or 0

    def get_remaining_amount(self, obj):
        total_sponsorship = self.get_total_sponsorship_amount(obj)
        total_contract = self.get_total_student_contract_amount(obj)
        return total_contract - total_sponsorship


