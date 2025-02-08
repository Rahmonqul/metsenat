from .serializers import SponsorshipSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Sponsorship
from rest_framework import status
from django.shortcuts import get_object_or_404
from students.models import Student
from sponsor.models import Sponsor
from django.utils.timezone import now
from django.db.models.functions import TruncMonth
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .serializers import SummarySerializer

# Create your views here.
class SponsorshipForStudentView(ListCreateAPIView):
    serializer_class = SponsorshipSerializer

    def get_queryset(self):
        student_id = self.kwargs.get("pk")
        return Sponsorship.objects.filter(student_id=student_id).select_related("sponsor", "student")

    def create(self, request, *args, **kwargs):
        student_id = self.kwargs.get("pk")
        student = get_object_or_404(Student, id=student_id)

        data = request.data.copy()

        sponsor_id = data.get("sponsor")
        if not sponsor_id:
            return Response({"sponsor": "Это поле обязательно."}, status=status.HTTP_400_BAD_REQUEST)

        sponsor = get_object_or_404(Sponsor, id=sponsor_id)

        amount = float(data.get("amount", 0))
        if amount > sponsor.sponsorship:
            return Response(
                {"amount": "Сумма не может превышать сумму спонсорства."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)


        sponsorship = serializer.save(student=student)


        sponsor.status = "Moderatsiyada"
        sponsor.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SponsorshipDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = SponsorshipSerializer
    queryset = Sponsorship.objects.select_related("sponsor", "student")

    def perform_destroy(self, instance):
        sponsor = instance.sponsor
        instance.delete()

        if not sponsor.sponsorships.exists():
            sponsor.status = "Yangi"
            sponsor.save()


class StatusAPIView(APIView):
    def get(self, request):

        months = [
            "Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun",
            "Iyul", "Avgust", "Sentabr", "Oktabr", "Noyabr", "Dekabr"
        ]

        current_year = now().year


        student_data = (
            Student.objects.filter(date__year=current_year)
            .annotate(month=TruncMonth("date"))
            .values("month")
            .annotate(count=Count("id"))
            .order_by("month")
        )

        sponsor_data = (
            Sponsor.objects.filter(date__year=current_year)
            .annotate(month=TruncMonth("date"))
            .values("month")
            .annotate(count=Count("id"))
            .order_by("month")
        )


        students_count = [0] * 12
        sponsors_count = [0] * 12

        for item in student_data:
            month_index = item["month"].month - 1  # Получаем индекс месяца (0-11)
            students_count[month_index] = item["count"]

        for item in sponsor_data:
            month_index = item["month"].month - 1
            sponsors_count[month_index] = item["count"]


        return Response({
            "months": months,
            "students": students_count,
            "sponsors": sponsors_count
        })



class SummaryAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        data = SummarySerializer(instance={}).data
        return Response(data)


