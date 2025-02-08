from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Sponsor
from .serializers import SponsorSerializer, SponsorDetailSerializer
from rest_framework.pagination import PageNumberPagination
from .filters import SponsorFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny
# from django.core.cache import cache

class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class SponsorListCreateView(ListCreateAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorSerializer
    pagination_class = Pagination
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_class = SponsorFilter
    permission_classes = [AllowAny]
    search_fields=['full_name', 'phone', 'sponsorship', 'status', 'company_name']


class SponsorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Sponsor.objects.all()
    serializer_class = SponsorDetailSerializer
