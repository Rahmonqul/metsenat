from django.urls import  path
from .views import SponsorshipForStudentView, SponsorshipDetailView, StatusAPIView, SummaryAPIView

urlpatterns=[
    path('student/<int:pk>/sponsorship/', SponsorshipForStudentView.as_view(), name='sponsorship-detail'),
    path('sponsorship/<int:pk>/', SponsorshipDetailView.as_view(), name='sponsorship-detail'),
    path('status/', StatusAPIView.as_view(), name='status-summa'),
    path('summary/', SummaryAPIView.as_view(), name='summary')
]