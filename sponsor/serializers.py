from rest_framework import serializers
from sponsor.models import Sponsor
from sponsorship.models import Sponsorship
from django.db.models import Sum

class SponsorSerializer(serializers.ModelSerializer):
    amount_spent = serializers.SerializerMethodField()
    linkdetail=serializers.SerializerMethodField()
    class Meta:
        model = Sponsor
        fields = ['full_name', 'phone', 'status', 'sponsor_type', 'sponsorship', 'amount_spent', 'company_name', 'date', 'linkdetail']
        read_only_fields=['status','date']

    def get_linkdetail(self, obj):
        request = self.context.get('request')
        if request:
            return request.build_absolute_uri(f"/api/sponsor/{obj.id}/")
        return f"/api/sponsor/{obj.id}/"

    def get_amount_spent(self, obj):
        total_spent = Sponsorship.objects.filter(sponsor=obj).aggregate(Sum('amount'))['amount__sum']
        return total_spent or 0

    def validate(self, data):
        if data['sponsor_type'] == 'Yuridik shaxs' and not data.get('company_name'):
            raise serializers.ValidationError({'company_name': 'Название компании обязательно для юридического лица.'})
        if data['sponsor_type'] == 'Jismoniy shaxs' and data.get('company_name'):
            raise serializers.ValidationError({'company_name': 'Физическое лицо не может иметь название компании.'})
        return data


class SponsorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ['full_name', 'phone', 'status', 'sponsor_type', 'sponsorship', 'type_payment', 'company_name']

    def validate(self, data):
        if data['sponsor_type'] == 'Yuridik shaxs' and not data.get('company_name'):
            raise serializers.ValidationError({'company_name': 'Название компании обязательно для юридического лица.'})
        if data['sponsor_type'] == 'Jismoniy shaxs' and data.get('company_name'):
            raise serializers.ValidationError({'company_name': 'Физическое лицо не может иметь название компании.'})
        return data